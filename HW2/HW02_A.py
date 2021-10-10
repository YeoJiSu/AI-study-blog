# 202055565 HW02_A_여지수 과제

#list를 string으로 입력 받아 strList에 저장
strList=input("Enter a number as a list : ")
#strList의 양끝 '[' 과 ']' 를 없애고 ','를 기준으로 잘라서 list로 변환
myList=strList[1:len(strList)-1].split(",")
#map을 이용하여 string list를 int list 형태로 변형 
myList=list(map(int,myList))

#myList를 크기 순으로 정렬
myList.sort()

#myList의 원소 개수를 len에 저장 
length = len(myList)

#len이 홀수라면 중앙값은 가운뎃 값이므로 중앙값을 median에 저장
len2 = int(length/2)
if length %2!=0:
    median = myList[len2]
#len이 짝수라면 가운데 두수의 평균이 중앙값이므로 이를 median에 저장
else:
    median = (myList[len2-1]+myList[len2])/float(2)

#%를 이용하여 포멧에 맞게 출력
print("Median: %0.1f"%median)
