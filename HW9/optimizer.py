from typing import ByteString
from setup import Setup
import random, math
class Optimizer(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._numExp = 0
        self._epsilon =0.01
        
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
        HillClimbing.displaySetting(self)
        
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
                
    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]
    
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
            
            if (valueN - valueC) < 0:
                current = neighbor
                valueC = valueN 
            elif random.uniform(0,1) < math.exp(-1*(valueN - valueC)/t):
                current = neighbor
                valueC = valueN
            
            if valueC < valueBest:
                (best, valueBest) = (current, valueC)
                whenBestFound = i
                
        self._whenBestFound = whenBestFound                
        p.storeResult(best,valueBest)
        f.close()
class GA(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def setVariables(self, parameters):
        MetaHeuristics.setVariables(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        if self._pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self._pType == 2:
            self._pC = self._XR
            self._pM = self._mR

    def displaySetting(self):
        print()
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristics.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self._pType == 1:   # Numerical optimization
            print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self._pType == 2: # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)

    
    
    # 1. Chromosome design
    # 2. Initialization
    def run(self, p):
        p.setNumEval()
        numEval = p.getNumEval()
        # population을 만들어 초기화 한다.
        popSize = self._popSize
        pop = p.initializePop(popSize)
        # 이때 pop을 프린트해보면 앞에 0이 들어가고 뒤에 array가 나오는 배열의 형식을 취하고 있다. 
        best = self.evalAndFindBest(pop, p) # fitness evaluation하여 0의 fitness 값을 바꾸어주어함
        
        while numEval < self._limitEval :
            newPop = []
            i = 0
            while i < popSize:
                par1, par2 = self.selectParents(pop)
                ch1, ch2 = p.crossover(par1, par2, self._pC)
                # mutation
                m1 = p.mutation(ch1, self._pM)
                m2 = p.mutation(ch2, self._pM)
                newPop.extend([m1, m2])
                i += 2
            pop = newPop
            newBest =self.evalAndFindBest(pop,p)
            numEval = p.getNumEval()
            # 새로 구한 값이 더 작으면 새로 구한 값으로 바꾼다. 
            if newBest[0] < best[0]:
                best = newBest
                whenBestFound = numEval
        bestSolution = p.indToSol(best)
        self._whenBestFound = whenBestFound
        # 구한 변수를 저장한다. 
        p.storeResult(bestSolution, best[0])
        
               
    # 3. Fitness evaluation
    def evalAndFindBest(self, pop, p):
        # pop의 chromosome에 대하여 evaluation을 함
        best = pop[0]
        p.evalInd(best)
        bestValue = best[0]
        for i in range(1, len(pop)):
            p.evalInd(pop[i])
            new = pop[i][0]
            if new < bestValue:
                best = pop[i]
                bestValue = new
        return best
    
    # 4. Selection
    def selectParents(self, pop):
        ind1, ind2 = self.selectTwo(pop)
        # ind1 과 ind2 중 작은 값이 par1
        par1 = self.binaryTournament(ind1, ind2)
        # 랜덤하게 다시 ind1, ind2를 설정한 후 
        ind1, ind2 = self.selectTwo(pop)
        # ind1 과 ind2 중 작은 값이 par2
        par2 = self.binaryTournament(ind1, ind2)
        return par1, par2
    
    def selectTwo(self, pop):
        popCopy = pop[:]
        # 랜덤하게 섞는다
        random.shuffle(popCopy)
        return popCopy[0], popCopy[1]
    
    def binaryTournament(self, ind1, ind2):
        if ind1[0] < ind2[0]:
            # 둘중 더 작은 것을 return 하는 함수 
            return ind1
        else:
            return ind2    
    
        