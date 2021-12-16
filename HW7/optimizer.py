from setup import Setup

class HillClimbing(Setup):
    def __init__(self):
        Setup.__init__(self)
        #limit-stuck 정의 
        self._limitStuck=100
        #epsilon 정의
        self._epsilon = 0.0001
        # pType 과 aType 초기화 해두기 
        self._pType=0
        self._aType=0
        
    def setVariables(self, aType, pType):
        self._aType = aType
        self._pType = pType
    
    def displaySetting(self):
        print()
        print("Search algorithm: ",end='')
       
        
# SteepestAscent 알고리즘 작성 
class SteepestAscent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        super().displaySetting();
        print("Steepest-Ascent")
        if self._pType==1:
            # numeric 일때 mutation step size return 하기 
            print()
            # Setup에서 받아온 delta 값 프린트하기 
            print("Mutation step size:", self._delta)

    def run(self, p):
        current = p.randomInit()   # 'current' is a list of city ids
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            (successor, valueS) = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
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
        super().displaySetting()
        print("First-Choice")
        if (self._pType==1):
            # numeric 일때 mutation step size return 하기 
            print()
            # Setup에서 받아온 delta 값 프린트하기 
            print("Mutation step size:", self._delta)
        
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)
        
# GradientDescent 알고리즘 작성 
class GradientDescent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)
        
    def displaySetting(self):
        super().displaySetting()
        print("Gradient Descent")
        print()
        print("Update rate: ", self._alpha)
        print("Increment for calculating derivatives:", self._epsilon)

        
    def run(self, p):
        ###########여기 
        current = p.randomInit() # current는 value 들의 list이다. 
        valueC = p.evaluate(current)
        
        while True: 
            # gradient 변수에 원소들의 미분 값들을 저장한 배열을 저장 합니다. 
            gradient = p.gradient(current, valueC,self._epsilon)
            # 원소들을 미분값만큼 감소한 것을 저장합니다. 
            nextP  = p.takeStep(gradient, current)
            nextN = p.evaluate(nextP)
            # valueC가 nextN 보다 같거나 크다면 current를 gradient에 의해 변경된 값으로 바꾸어줍니다. 
            if  nextN <= valueC:
                current = nextP
                valueC = nextN
            else:
                break
        p.storeResult(current, valueC)
        
 
