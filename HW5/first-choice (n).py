from numeric import *

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': [expr, domain]
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p):
    #i, d를 랜덤으로 적음 
    # i는 0부터 current의 길이-1까지의 정수 중 하나로 랜덤하게 구하고 
    i = random.randint(0,len(current)-1)
    # d는 DELTA와  -DELTA 중 하나이므로 아래와 같이 랜덤하게 구합니다.
    delta = [DELTA, -DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
