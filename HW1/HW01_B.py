# 202055565 여지수 HW01_B_(여지수)
# input을 통해 beginning_salary를 입력받습니다.
beginning_salary = float(input("Enter beginning salary: "))

# new_salary는 beginning_salary를 10%만큼 세번 인상시킨 가격이므로 다음과 같이 식을 적습니다. 
new_salary = beginning_salary * (1+0.1)**3

# change는 beginning_salary에 대한 "new_salary과 beginning_salary의 급여 차" 비율 입니다. 
change= (new_salary-beginning_salary) / beginning_salary * 100

# format을 이용해 소수점 둘째자리 까지, 그리고 숫자 3자리마다 콤마를 넣습니다. 
print("New salary: ${0:,.2f}".format(new_salary))
print("Change: {0:.2f}%".format(change))
