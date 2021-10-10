# 202055565 여지수 HW01_D_(여지수)

# input을 이용하여 coefficient와 initial height를 입력 받습니다. 
coef = float(input("Enter coefficient of restitution: "))
height = float(input("Enter initial height in meters: "))

# 전체 bounce 횟수를 저장할 변수 num을 0으로 초기화 합니다. 
num=0

# 처음 떨어뜨리는 지점(미터 m)을 100을 곱해서 cm로 변환합니다. 
height*=100

# 전체 움직인 높이들의 합을 저장하는 변수 sum을 처음 높이로 초기화 합니다.
sum = height

while (True): # 높이가 10cm 이하가 되기 전까지 이 while문은 반복됩니다. 
    height *= coef # 높이에 계수를 곱해줍니다. 
    num+=1  # 튕긴 횟수를 한개씩 늘려줍니다. 
    if height <= 10 : break # 조건문을 걸어, 높이가 10cm 이하가 되기 전까지 움직인 높이들의 합의 2배를 sum에 저장합니다. 
    sum+=height *2 # 2배인 이유는 위 + 아래로 움직인 합을 더해야 하기 때문입니다.

# format을 이용해 주어진 형식대로 출력되도록 합니다. 
print("Number of bounces: {}".format(num))
print("Meters traveled: {0:.2f}".format(sum/100))
