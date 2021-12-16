from setup import Setup
import random, math
class Optimizer(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._numExp = 0
        
    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']  
        self._numExp = parameters['numExp']
        
    def getNumExp(self):
        return self._numExp
    
    def displayNumExp(self):
        print()
        print("Number of Experiments:", self._numExp)
        
    def displaySetting(self):
        if self._pType == 1 and self._aType !=4 and self._aType != 6:
            print("Mutation step size", self._delta)
    
   
    
class HillClimbing(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self._limitStuck=100 # Max evaluations with no improvement
        self._numRestart = 0
        
        # #epsilon 정의
        # self._epsilon = 0.0001
        # # pType 과 aType 초기화 해두기 
        # self._pType=0  # Problem type
        # self._aType=0
        
    def setVariables(self, parameters):
        Optimizer.setVariables(self, parameters)
        self._limitStuck = parameters['limitStuck']
        self._numRestart = parameters['numRestart']
    
    def displaySetting(self):
        if self._numRestart >=1:
            print("Number of random restarts:", self._numRestart)
            print()
        if 2<= self._aType <=3:
            print("Max evaluations with no imporvements: {0:,}.".format(self._limitStuck))
    
    def run(self):
        pass
    
    def randomRestart(self, p):
        i = 1
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()
        while i < self._numRestart :
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval = p.getNumEval()
            if newMinimum < bestMinimum:
                bestSolution = newSolution
                bestMinimum = newMinimum
            i+=1
        p.storeResult(bestSolution, bestMinimum)   
        
    # def getAType(self):
    #     return self._aType
        
# SteepestAscent 알고리즘 작성 
class SteepestAscent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        HillClimbing.displaySetting(self)
        Optimizer.displaySetting(self)

    def run(self, p):
        current = p.randomInit()   # 'current' is a list of city ids
        valueC = p.evaluate(current)
        f = open('steepest.txt', 'w')
        while True:
            neighbors = p.mutants(current)
            (successor, valueS) = self.bestOf(neighbors, p)
            f.write(str(round(valueC,1))+'\n')
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        f.close()
        p.storeResult(current, valueC)
        
    def bestOf(self, neighbors, p):
        # 모두다 evaluation을 해봄 
        # 우선은 neighbors의 0번째 원소를 best에 저장하고
        # 그 0번째 원소를 가지고 p를 evaluate 한 값을 bestValue에 저장한다.
        best = neighbors[0]
        bestValue = p.evaluate(best)
        # neighbors안에 있는 모든 원소에 대해 for 문을 돌리는 데 
        for i in neighbors:
            new_value = p.evaluate(i)
            # 초기 설정했던 bestValue보다 새로 생성한 new_value 값이 더 작다면 
            # bestValue 값과 best 값을 더 작은 수로 바꾼다.
            # 그리고 for문을 계속해서 돌리면서 작은 수가 나타난다면 계속 바꾸어 준다.
            if new_value < bestValue:
                best = i
                bestValue = new_value
        return best, bestValue

# FirstChoice 알고리즘 작성 
class FirstChoice(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)
        
    def displaySetting(self):
        HillClimbing.displaySetting(self)
        Optimizer.displaySetting(self)
        
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        f = open('first.txt','w')
        
        while i < self._limitStuck:
            f.write(str(valueC)+'\n')
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        f.close()
        p.storeResult(current, valueC)
        
# GradientDescent 알고리즘 작성 
class GradientDescent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)
        
    def displaySetting(self):
        HillClimbing.displaySetting(self)
        Optimizer.displaySetting(self)
        print("Gradient Descent")
        print()
        print("Update rate: ", self._alpha)
        print("Increment for calculating derivatives:", self._epsilon)

        
    def run(self, p):
        current = p.randomInit() # current는 value 들의 list이다. 
        valueC = p.evaluate(current)
        
        while True: 
            # gradient 변수에 원소들의 미분 값들을 저장한 배열을 저장 합니다. 
            gradient = p.gradient(current, valueC,self._epsilon)
            # 원소들을 미분값만큼 감소한 것을 저장합니다. 
            nextP  = p.takeStep(gradient, current)
            nextN = p.evaluate(nextP)
            # valueC가 nextN 보다 같거나 크다면 current를 gradient에 의해 변경된 값으로 바꾸어줍니다. 
            if valueC >= nextN:
                current = nextP
                valueC = nextN
            else:
                break
        p.storeResult(current, valueC)
        
        
class Stochastic(HillClimbing):
    def displaySetting(self):
        print()
        print("Search Algorithm: Stochastic Hill Climbing")
        print()
        HillClimbing.displaySetting()
        
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i<self._limitStuck:
            neighbors = p.mutants(current)
            successor, valueS = self.stochasticBest(neighbors,p)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current,valueC) 
    
    #### 제공된 코드 #####
    def stochasticBest(self, neighbors, p):
        Min = [p.evaluate(x) for x in neighbors]
        Max = [max(Min)+1-x for x in Min]
        
        rand = random.uniform(0,len(Max))
        s= Max[0]
        
        for i in range(len(Max)):
            if rand<=s :
                break
            else:
                s += Max[i+1]
            
        return neighbors[i], Min[i]
            
    
class MetaHeuristics(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self._limitEval = 0
        self._whenBestFound = 0
    
    def setVariables(self, parameters):
        Optimizer.setVariables(self, parameters)
        self._limitEval = parameters['limitEval']
        
    def getWhenBestFound(self):
        return self._whenBestFound
    
    def displaySetting(self):
        Optimizer.displaySetting(self)
        print("Number of evaluations until termination: {0:,}".format(self._limitEval))
    
    def run(self):
        pass
    
class SimulatedAnnealing(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._numSample = 100
        
    def displaySetting(self):
        print()
        print("Search Algorithm: Simulated Annealing")
        print()
        MetaHeuristics.displaySetting(self)
        
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        
        best, valueBest = current, valueC
        whenBestFound = i = 1
        
        f = open('anneal.txt','w')
        
        t = self.initTemp(p)
        
        while True:
            f.write(str(valueC) + '\n')
            t = self.tSchedule(t)
            if t == 0 or i == self._limitEval:
                break
            neighbor = p.randomMutant(current)
            valueN = p.evaluate(neighbor)
            i+=1
            
            if valueN < valueC:
                current = neighbor #똑같
                valueC = valueN 
            elif random.uniform(0,1) < math.exp(-1*(valueN - valueC)/t):
                current = neighbor
                valueC = valueN # 똑같
            
            if valueC < valueBest:
                (best, valueBest) = (current, valueC)
                whenBestFound = i
                
        self._whenBestFound = whenBestFound                
        p.storeResult(best,valueBest)
        f.close()
  
        
    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))
        
