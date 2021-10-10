# 202055565 여지수 HW01_C_(여지수)

# 전체 합을 입력할 변수 sum을 0으로 초기화 합니다. 
sum = 0

# 1부터 100만까지 숫자에 대해 자릿수의 합을 구할 것이므로 우선 각 숫자에 대한 loop문을 작성합니다. 
for number in range(1,10**6+1):
    # 각숫자를 문자열로 바꾸어 줍니다 
    number=str(number)
    # 각 숫자에 대한 자릿수 합을 변수 digit으로 설정하고 0으로 초기화 합니다. 
    digit = 0
    for j in number: # 문자열안의 문자들을 int로 변환한 후 하나씩 더하면 자릿수 합이 digit에 저장됩니다. 
        digit += int(j)
    sum += digit # 그 digit들의 합이 sum에 저장됩니다.
    
# format 형식을 이용해 숫자 3자리마다 콤마를 넣습니다.  
print("The sum of the digits in the numbers \nfrom 1 to one million is {0:,}.".format(sum))
