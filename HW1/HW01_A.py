# 202055565 여지수 HW01_A_(여지수)
# input을 통해 purchase_price와 selling_priced를 입력받습니다. 
purchase_price = float(input("Enter purchase price: "))
selling_price = float(input("Enter selling price: "))

# markup은 selling_price와 purchase_price의 차이라고 했으므로 아래와 같이 나타냅니다.
markup = selling_price - purchase_price
print("Markup: ${0:.1f}".format(markup))

# percentage_markup과 profit_margin은 문제에 제시된 공식을 이용해 작성합니다.
# format 형식을 이용해 소수점 첫째자리 또는 둘째자리 까지 출력되도록 합니다. 
percentage_markup = markup / purchase_price *100
print("Percentage markup: {0:.1f}%".format(percentage_markup))

profit_margin = markup / selling_price *100
print("Profit margin: {0:.2f}%".format(profit_margin))
