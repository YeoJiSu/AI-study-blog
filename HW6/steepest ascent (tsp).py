from tsp import *
def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': [numCities, locations]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC
def mutants(current, p): # Inversion only
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors
def bestOf(neighbors, p):
    # 모두다 evaluation을 해봄 
    # 우선은 neighbors의 0번째 원소를 best에 저장하고
    # 그 0번째 원소를 가지고 p를 evaluate 한 값을 bestValue에 저장한다.
    best = neighbors[0]
    bestValue = evaluate(best,p)
    # neighbors안에 있는 모든 원소에 대해 for 문을 돌리는 데 
    for i in neighbors:
        new_value = evaluate(i,p)
        # 초기 설정했던 bestValue보다 새로 생성한 new_value 값이 더 작다면 
        # bestValue 값과 best 값을 더 작은 수로 바꾼다.
        # 그리고 for문을 계속해서 돌리면서 작은 수가 나타난다면 계속 바꾸어 준다.
        if new_value < bestValue:
            best = i
            bestValue = new_value
    return best, bestValue
def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
main()
