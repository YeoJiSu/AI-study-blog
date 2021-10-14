def displaySequenceNumbers(m,n):
    #마지막 수를 변수 last에 저장합니다.
    last=n
    # n 이 m과 일치하지 않다면 아래를 수행합니다.
    if (n!=m):
        # n을 1만큼 감소시키고, 다시 자기자신function을 불러옵니다.
        n-=1
        displaySequenceNumbers(m,n)
        # 그러면 n이 m과 일치할때까지 n을 출력합니다. 
        print(n)
    # 위의 코드에서 n을 1만큼 줄인 후부터 출력되게 하였으므로
    # 마지막 수를 리턴하여 main에서 print()함수를 썼을 때 모든 수가 다 print되도록 합니다. 
    return last
    
def main():
    print ("output of print (displaySequenceNumbers(2,4))")
    print (displaySequenceNumbers(2,4))
    print ("output of print (displaySequenceNumbers(3,3))")
    print (displaySequenceNumbers(3,3))

main()
