import random
import math

NumEval = 0    # Total number of evaluations

def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
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
    return numCities, locations, table

def calcDistanceTable(numCities, locations):
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

