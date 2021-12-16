import random
import math
from setup import Setup

class Problem(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._solution = []
        self._value = 0
        self._numEval = 0
        
        
    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pFileName = parameters['pFileName']
        
        
    # 맴버 변수들의 get, set 함수들을 만들어 줍니다. 
    def getNumEval(self):
        return self._numEval
    def getSolution(self):
        return self._solution
    def getValue(self):
        return self._value
    
    def setNumEval(self, cnt = 0):
        self._numEval += cnt
    
    def storeResult(self, solution,value):
        self._solution = solution
        self._value = value
    
    def storeExpResult(self, results):
        self._bestSolution = results[0]
        self._bestMinimum = results[1]
        self._avgMinimum = results[2]
        self._avgNumEval = results[3]
        self._sumOfNumEval = results[4]
        self._avgWhen = results[5]    
        
        
    #numeric과 tsp의 공통적인 부분 구현 =>
    # def report(self):
    #     print()
    #     print("Total number of evaluations: {0:,}".format(self.getNumEval()))
    
    def report(self):
        aType = self._aType
        if 1 <= aType <=4:
            print("Average number of evaluationis: {0:,}".format(round(self._avgNumEval)))
        if 5 <= aType <= 6:
            print("Average iteration of finding the best: {0:,}".format(self._avgWhen))
        print()
        
    def reportNumEvals(self):
        if 1 <= self._aType <= 4:
            print()
            print("Total number of evaluations: {0:,}".format(self._sumOfNumEval))


class Numeric(Problem):
    # report에서 마저 못한 부분 override 받아야 함 
    def __init__(self):
        Problem.__init__(self)
        self._delta = 0.01
        self._domain = []
        self._expression = ''
        
        # gradient_decent를 위한 초기화
        self._dx = 0.01
        self._alpha = 0.01

    def getDelta(self):
        return self._delta
    def getAlpha(self):
        return self._alpha
    def getDx(self):
        return self._dx
    
    # 이전 과제에서 구현한 createProblem()을 setVariables()로 구현함 
    def setVariables(self,parameters):
        Problem.setVariables(self,parameters)
        infile = open(self._pFileName, 'r')
        expression = infile.readline() 
        # 파일의 첫번째 줄이 식이므로 이를 읽어와 expression 변수에 저장한다.  
        varNames=[] # 변수들을 저장할 list
        low=[] # 각 변수들의 범위 최솟값을 저장할 list
        up=[] # 각 변수들의 범위 최댓값을 저장할 list
        
        # 그 다음줄 부터 변수, 최소범위, 최대범위를 저장해야하므로 while 문을 이용해 모두 저장합니다. 
        line = infile.readline()
        # 다음줄이 없을 때까지 계속해서 다음줄을 읽어오고 
        # ","를 기준으로 잘라 리스트를 만들었을 떄 0번쨰는 변수, 1번째는 최소범위, 2번째는 최대범위 입니다. 
        while line !="":
            v=line.split(',')[0]
            l=float(line.split(',')[1])
            u=float(line.split(',')[2])
            # 각각의 리스트에 모두 append 합니다. 
            varNames.append(v)
            low.append(l)
            up.append(u)
            line = infile.readline()
        infile.close()
        # domain에 저장한 각각의 변수이름, 최소, 최대 리스트를 모두 저장합니다. 
        self._domain=[varNames,low,up]  
        self._expression = expression
        
    def randomInit(self): # Return a random initial point as a list
        # 원래의 randomInit의 매개변수 p[1]은 domain 이였으므로 domain 을 받아와 정의한다. 
        domain = self._domain
        low,up = domain[1],domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.randrange(low[i],up[i]))
        return init

    def evaluate(self, current):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        
        self._numEval+=1
        expr = self._expression         # p[0] 는 expression 이였으므로 바꿔줌
        varNames = self._domain[0]  # p[1] 은 domain 이였음  [varNames, low, up]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = self._domain       # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 

    def displayResult(self, solution, minimum):
        print()
        print("Solution found:")
        print(self.coordinate(solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(minimum))
        super().report()
        super().reportNumEvals()

    def coordinate(self, solution):
        c = [round(value, 3) for value in solution]
        return tuple(c)  # Convert the list to a tuple

# first-choice (n)
    def randomMutant(self, current):
        #i, d를 랜덤으로 적음 
        # i는 0부터 current의 길이-1까지의 정수 중 하나로 랜덤하게 구하고 
        i = random.randint(0,len(current)-1)
        # d는 DELTA와  -DELTA 중 하나이므로 아래와 같이 랜덤하게 구합니다.
        delta = [self._delta, -self._delta]
        d = random.choice(delta)
        return self.mutate(current, i, d)

# steepest ascent (n)
    def mutants(self, current):
        # 빈 배열  neighbors  생성
        neighbors = []
        # i 가 0 부터  current의 길이 -1 까지 반복문을 돌림.
        for i in range(0,len(current)):
            # 전체 i에 대해 DELTA 일 때 -DELTA일 때 모두 mutate 하여 neighbor list에 추가합니다.
            neighbors.append(self.mutate(current, i, self._delta))
            neighbors.append(self.mutate(current, i, -self._delta))
        # 생성한 list를 return 합니다.
        return neighbors

    # gradient_descent
    def gradient(self,current, valueC, epsilon):
        # 우선, 원소들의 미분값을 저장할 배열을 선언합나디ㅏ.
        gradient = []
        domain = self._domain
        for i in range(len(current)):
            low = domain[1][i]
            up = domain[2][i]
            value = current[i]
            # current는 현재 배열로 현재 배열 속 원소를 value 에 저장합니다. 
            derivate = current[:i]
            # derivate이라는 새 배열에 0부터 현재 이전까지의 원소들을 저장합니다. 
            
            # 현재 원소 값+ 알파 값이 low 이상 up 이하 일 떼 현재 원소가 저장된 value값을 증가시킵니다.  
            if (low <= current[i]+ epsilon <= up):
                value = value + epsilon
            # derivate 배열에 value 값을 넣고, i 뒤의 모든 원소들을 넣습니다.
            derivate.append(value)
            derivate.extend(current[i+1:])
            # gradient 배열에 알고리즘 값을 계산하여 넣습니다. 
            gradient.append((self.evaluate(derivate)-valueC)/epsilon)
        return gradient
    
    def takeStep(self, gradient, current):
        # 빈배열 suc를 선언합니다.
        suc = []
        # 모든 원소들에 대해 각각의 미분한 값 만큼 감소한 값을 suc 변수가 추가해 넣습니다. 
        for i in range(len(current)):
            suc.append(current[i]- self._alpha*gradient[i])
        return suc
        
class Tsp(Problem):
    # return type이 none 
    def __init__(self) -> None:
        super().__init__()
        self._numCities =0
        self._locations = []
        self._table = []

        
    # 이전 과제에서 구현한 createProblem()을 setVariables()로 구현함 
    def setVariables(self, parameters):
        Problem.setVariables(self, parameters)
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')
        # First line is number of cities
        numCities = int(infile.readline())
        locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            locations.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        #print(numCities,locations)
        table = self.calcDistanceTable(numCities, locations)
        
        #return numCities, locations, table
        self._numCities = numCities
        self._locations = locations
        self._table = table

    def calcDistanceTable(self, numCities, locations):
        # 빈 테이블을 하나 생성합니다. 
        table = []
        # 도시 수만큼 중첩 for을 돕니다. 도시수 X 도시수 테이블 이므로
        for i in range(numCities):
            # 도시수를 한번 돌아 distance가 계산될때마다 리스트가 2차원으로 추가되는 것이므로 line이라는 빈 리스트를 생성합니다.
            line = []
            for k in range(numCities):
                # 두 도시의 locations의 x좌표 차 제곱 + y좌표 차 제곱 에 루트를 씌운 것이 거리이므로 다음과 같이 계산합니다.
                distance = math.sqrt((locations[i][0]-locations[k][0])**2 + (locations[i][1]-locations[k][1])**2)
                # line 이라는 배열에 각각의 distance를 저장하고
                line.append(distance)
            # line들을 테이블에 모두 저장합니다.
            table.append(line)
        ###
        return table # A symmetric matrix of pairwise distances

    def randomInit(self):   # Return a random initial tour
        # 원래 p[0]는 numCities 였음.
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        
        self._numEval+=1
        # cost를 0으로 초기화 합니다.
        cost = 0
        # p에는 numCities, locations, table 가 저장되어있으므로 아래와 같이 정의합니다.
        table= self._table
        # 도시의 수만큼 반복문을 돌립니다.
        for i in range(len(current)):
            if i == (len(current)-1):
                break
            # 랜덤 index 리스트인 current를 이용하여 모든 city에 한번씩 갈 수 있는 cost들을 모두 더합니다.
            cost += table[current[i]][current[i-1]]
        #or i in range
        return cost

    def inversion(self, current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describe(self):
        print()
        # 원래 p[0]은 numCities 였음.
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        # 원래 p[1]은 loactions 였음.
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def displayResult(self, solution, minimum):
        print()
        print("Best order of visits:")
        self.tenPerRow(solution)       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(minimum)))
        super().report()
        super().reportNumEvals()

    def tenPerRow(self, solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()
    # first-choice (tsp)
    def randomMutant(self,current): # Inversion only
        while True:
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    # steepest ascent (tsp)
    def mutants(self,current): # Inversion only
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

        