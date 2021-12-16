import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


def createProblem():
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
    # domain에 저장한 각각의 변수이름, 최소, 최대 리스트를 모두 저장합니다. 
    infile.close()
    domain=[varNames,low,up]  
    return expression, domain

def randomInit(p): # Return a random initial point as a list
    # randomInit의 매개변수 p에는 expression, domain 이 입력됩니다.
    expression, domain = p
    # 우리는 domain안에 있는 변수들을 각각의 범위에 해당하는 랜덤한 수를 뽑아내야합니다. 
    init=[]
    for i in range(0,len(domain[0])):
        # 최소와 최대 사이 랜덤한 float을 저장합니다.
        init.append(random.uniform(domain[1][i],domain[2][i]))
    return init    # list of values

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
    return curCopy # 돌연변이 리스트를 반환

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

