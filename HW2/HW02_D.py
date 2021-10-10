# 202055565 HW02_D_여지수 과제
# 연 이자율, 월 지급액, 월 잔액을 매개변수로 받는 calculateValues 함수를 생성.
def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):
    # " 월 잔액 * (연 이자율/12) " 값을 가지는 매월 지급되는 이자를 변수 intForMonth에 저장.
    intForMonth= begBalance*(annualRateOfInterest/100/12.0)
    # " 월 지급액 - 매월 지급되는 이자 " 값을 가지는 월 원금 감면은 변수 redOfPrincipal에 저장.
    redOfPrincipal = monthlyPayment-intForMonth
    # " 월 잔액 - 월 원금 감면 " 값을 가지는 월말잔액은 변수 endBalance에 저장.
    endBalance = begBalance - redOfPrincipal
    
    # intForMonth: Interest paid for the month
    # redOfPrincipal: Reduction of principal
    # endBalance: End of month balance
    return (intForMonth, redOfPrincipal, endBalance)

# input을 통해 연 이자율, 월 지급액, 월 잔액을 입력받아 각각 rate, payment, beg 변수에 저장 
rate = float(input("annual rate of interest: "))
payment = float(input("Enter monthly payment: "))
beg = float(input("Enter beg. of month balance: "))

# 위의 값들을 앞서 생성한 함수의 인자로 전달하여 함수의 return 값을 a,b,c 에 저장 
a,b,c = calculateValues(rate,payment,beg)

# format을 이용하여 소수점 둘쩨자리까지, 그리고 숫자 3자리마다 콤마 넣음
print("Interest paid for the month: ${0:,.2f}".format(a))
print("Reduction of principal: ${0:,.2f}".format(b))
print("End of month balance: ${0:,.2f}".format(c))

