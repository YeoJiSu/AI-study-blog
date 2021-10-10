# 202055565 HW02_C_여지수 과제

# 과제 A와 마찬가지로 list를 string으로 입력 받아 strList에 저장 
str1 = input("Input list = ")
# strList 의 양끝 '['과 ']'를 없애고 ','를 기준으로 잘라서 list로 변환 
myList=str1[1:len(str1)-1].split(",")
# map을 이용하여 string list를 int list로 변환 
myList = list(map(int, myList))
# myList를 크기 순으로 정렬 
myList.sort()

# frequency를 셀 0으로 초기화된 countList를 생성 
countList=[0]*10
# myList 원소의 빈도를 세서 countList에 값 저장  
for i in myList:
    countList[i]+=1

# 출력할 string을 str2로 선언하고 출력 형식에 맞게끔 출력 
str2='['
comma = ', '
for i in range(0,10):
    if i==9: comma =''
    # format 형식으로 출력 
    str2+='[{num}, {count}]'.format(num=i,count = countList[i])+comma
str2+=']'
print("Encoded list = {mylist}".format(mylist=str2))
