class Quizzes:
    def __init__(self, listOfGrades):
        # listOfGrades라는 인자를 받아 초깃값을 저장합니다.
        self._listOfGrades = listOfGrades
    def average(self):
        # 점수 합을 0으로 초기화하여 sum에 저장합니다. 
        sum=0
        # 6가지 수를 입력 받았으므로 for문을 사용하여 list에 들어있는 6가지 수들을 모두 더합니다. 
        for i in range(0,6):
            sum+=self._listOfGrades[i]
        # 가장 낮은 점수를 떨어뜨린다 하였으므로 list에서 가장 작은 값은 빼줍니다. 
        sum-=min(self._listOfGrades)
        # 5명 학생의 grade의 평균을 리턴합니다. 
        return sum/5
    def __str__(self):
        # 출력 포멧에 맞게 문자열을 만들어 return 합니다. 
        return ("Quiz average: {:.1f}".format(self.average()))

def main():
    #grade를 저장할 빈 리스트 listOfGrades를 선언합니다. 
    listOfGrades = []
    #grade 6개를 float 타입으로 입력받아 위에서 선언한 ㅣist에 하나씩 추가합니다. 
    for i in range(0,6):
         a = float(input("Enter grade on quiz 1: "))
         listOfGrades.append(a)
    #Quizzes에 생성한 리스트를 인자로 전달해 객체를 생성하여 q에 저장합니다. 
    q = Quizzes(listOfGrades)
    #__str__에 의해 q가 예제 출력대로 출력되게끔 합니다. 
    print (q)

main()
