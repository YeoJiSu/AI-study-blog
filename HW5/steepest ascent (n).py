from numeric import *
def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': [expr, domain]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else: # 새로구한 결과값이 더 작으면 현재값 갱신함 
            current = successor
            valueC = valueS
    return current, valueC

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

def bestOf(neighbors, p):
    # 빈 리스트 all을 생성합니다.
    all = []
    # i가 0부터 neighbors의 길이 -1 까지 반복문을 돌림.
    for i in range(0,len(neighbors)):
        # all list에 neighbors의 모든 경우에 대해 결과값 계산해서 넣음 
        all.append(evaluate(neighbors[i],p))
    # 최솟값을 bestValue에 저장합니다. 
    bestValue=min(all)
    # 만들어진 list의 원소값중 최솟값의 index를 찾아 해당 index의 neighbors값을 best 에 저장합니다.
    best = neighbors[all.index(min(all))]

    return best, bestValue # 배열이랑 최소 결과값 반환함 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)
main()
