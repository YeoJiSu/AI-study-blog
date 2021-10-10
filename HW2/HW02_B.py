# 202055565 HW02_B_여지수 과제

# 네자리 수 중에서 special number을 찾을 것이므로 for문을 이용해서 네자리 수 숫자에 대해 반복문을 돌림
for num in range(1000,10000):
    # num의 4배 값을 string으로 변환하고 list형태로 변수 n_list에 저장
    n_list=list(str(4*num))
    # n_list를 뒤집음
    n_list.reverse()
    # join을 이용하여 뒤집은 n_list를 string으로 변환한 후 int로 변환하여 num2에 저장 
    num2=int("".join(n_list))
    # num과 num2 가 같다면 출력 포맷에 맞게 출력을 함 
    if num == num2:
        print("Since 4 x {0} is {1},\nthe special number is {1}.".format(num2,num2*4,num2*4))

    
