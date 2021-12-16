import random
import math


class Problem():
    def __init__(self) -> None:
        #_solution, _value, _numEval을 멤버 변수로 선언합니다. 
        self._solution = []
        self._value = 0
        self._numEval = 0
        
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
        
    #numeric과 tsp의 공통적인 부분 구현 =>
    def report(self):
        print()
        print("Total number of evaluations: {0:,".format(self._numEval))

class Numeric(Problem):
    # report에서 마저 못한 부분 override 받아야 함 
    def __init__(self) -> None:
        super().__init__()
        self._delta = 0.01
        self._domain = []
        self._expression = ''
        self._dx = 0.01
        self._alpha = 0.01
    
    
    # 이전 과제에서 구현한 createProblem()을 setVariables()로 구현함 
    def setVariables(self):
        fileName = input("Enter the file name of a function: ")
        infile = open(fileName, 'r')
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
        # randomInit의 매개변수 p에는 expression, domain 이 입력됩니다.
        domain = self._domain
        low,up = domain[1],domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.randrange(low[i],up[i]))
        return init

    def evaluate(current, p):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        global NumEval
        
        NumEval += 1
        expr = p[0]         # p[0] is function expression
        varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = p[1]        # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def describeProblem(p):
        print()
        print("Objective function:")
        print(p[0])   # Expression
        print("Search space:")
        varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
        low = p[1][1]
        up = p[1][2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 

    def displayResult(solution, minimum):
        print()
        print("Solution found:")
        print(coordinate(solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(minimum))
        print()
        print("Total number of evaluations: {0:,}".format(NumEval))

    def coordinate(solution):
        c = [round(value, 3) for value in solution]
        return tuple(c)  # Convert the list to a tuple

    def randomMutant(current, p):
        #i, d를 랜덤으로 적음 
        # i는 0부터 current의 길이-1까지의 정수 중 하나로 랜덤하게 구하고 
        i = random.randint(0,len(current)-1)
        # d는 DELTA와  -DELTA 중 하나이므로 아래와 같이 랜덤하게 구합니다.
        delta = [DELTA, -DELTA]
        d = random.choice(delta)
        return mutate(current, i, d, p)

    def mutants(current, p):
        # 빈 배열  neighbors  생성
        neighbors = []
        # i 가 0 부터  current의 길이 -1 까지 반복문을 돌림.
        for i in range(0,len(current)):
            # 전체 i에 대해 DELTA 일 때 -DELTA일 때 모두 mutate 하여 neighbor list에 추가합니다.
            neighbors.append(mutate(current, i, DELTA,p))
            neighbors.append(mutate(current, i, -DELTA,p))
        # 생성한 list를 return 합니다.
        return neighbors

    
class Tsp(Problem):
    # return type이 none 
    def __init__(self) -> None:
        super().__init__()
        self._numCities =0
        self._locations = []
        self._table = []
        
    
    def createProblem(self):
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
        table = calcDistanceTable(numCities, locations)
        
        #return numCities, locations, table
        self._numCities = numCities
        self._locations = locations
        self._table = table

    def calcDistanceTable(self,numCities, locations):
        # 빈 테이블을 하나 생성합니다. 
        table = self._table
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

    def randomInit(p):   # Return a random initial tour
        n = p[0]
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(current, p):
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        # 글로벌 변수 NumEval을 증가시킨다.
        global NumEval
        NumEval+=1 
        # cost를 0으로 초기화 합니다.
        cost = 0
        # p에는 numCities, locations, table 가 저장되어있으므로 아래와 같이 정의합니다.
        numCities, locations, table = p
        # 도시의 수만큼 반복문을 돌립니다.
        for i in range(numCities):
            # 랜덤 index 리스트인 current를 이용하여 모든 city에 한번씩 갈 수 있는 cost들을 모두 더합니다.
            cost += table[current[i]][current[i-1]]
        #or i in range
        return cost

    def inversion(current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describeProblem(p):
        print()
        n = p[0]
        print("Number of cities:", n)
        print("City locations:")
        locations = p[1]
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def displayResult(solution, minimum):
        print()
        print("Best order of visits:")
        tenPerRow(solution)       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(minimum)))
        print()
        print("Total number of evaluations: {0:,}".format(NumEval))

    def tenPerRow(solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()
        