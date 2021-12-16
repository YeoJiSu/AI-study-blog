from problem import *
from optimizer import *

def selectProblem():
    #사용자로부터 문제 유형을 입력 받음
    print("Select the problem type:")
    print(" 1. Numeric Optimization")
    print(" 2. TSP")
    pType = int(input("Enter the number: "))
    # 1이면 p 변수에 Numeric object를 저장한다. 
    if pType == 1:
        p= Numeric()
    # 2이면 p 변수에 Tsp object를 저장한다. 
    elif pType == 2:
        p= Tsp()
    return p, pType

def invalid(pType, aType):
    #TSP 문제는 GradientDescent를 쓸 수 없다.
    if (pType==2 and aType==3):
        print("You cannot choose Gradient Descent with TSP") 
        return False
    else:
        return True

def selectAlgorithm(pType):
    # 사용자로부터 알고리즘 유형을 입력 받음 
    print()
    print("Select the search algorithm: ")
    print("  1. Steepest-Ascent")
    print("  2. First-Choice")
    print("  3. Gradient Descent")  
    
    # 선택한 문제가 tsp이고 알고리즘이 Gradient Descent 이면 다시 입력을 받도록 한다. 
    while (True):
        aType = int(input("Enter the number: "))
        if (invalid(pType,aType)):
            break
        
    optimizers = {1: 'SteepestAscent()',
                  2: 'FirstChoice()',
                  3: 'GradientDescent()'}
    
    #eval 함수의 매개변수로 선택한 문자열 값을 넣어서 object가 실행되도록 합니다. 
    alg = eval(optimizers[aType])
    # setVariables 매소드를 불러와 aType과 pType을 저장합니다. 
    alg.setVariables(aType, pType)
    return alg

def main():
    p, pType = selectProblem() # 문제 유형 고르기 
    p.setVariables(); # 파일 이름 입력하기 
    alg = selectAlgorithm(pType) # 알고리즘 유형 고르기 
    alg.run(p) # 해당되는 함수 돌리고 
    p.describeProblem() # 출력 형식에 맞게 문제 출력하고 결과값들 출력하기 
    alg.displaySetting()
    p.displayResult(p._solution, p._value)
    
main()