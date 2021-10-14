# 랜덤하게 컴퓨터의 가위 바위 보를 생성할 것이므로 random을 import 합니다. 
import random
random.seed()
class Contestant:
    # name은 빈 string, score은 0이라는 default 값으로 초깃값을 설정합니다. 
    def __init__(self, name="", score=0):
        self.name= name
        self.score= score
    # name 게터를 만들고, 이때 string으로 name이 리턴되도록 cast 합니다. 
    def getName(self):
        return str(self.name)
    # score 게터를 만듭니다.  
    def getScore(self):
        return self.score
    # score이 1증가되도록 함수를 작성합니다.
    def incrementScore(self):
        self.score+=1
    # 상속 받은 함수에서 name을 return 하고 프린트할 때 string 타입으로 print 되어야 하므로 __str__ 함수를 작성합니다. 
    def __str__(self):
        return self.name

class Human(Contestant):
    def makeChoice(self):
        # 사람의 name을 받아와 가위 바위 보 중 무엇을 낼 것인지 입력 받도록 합니다. 
        name = self.getName()
        what=str(input("\n{0}, enter your choice: ".format(name)))
        # 입력 값을 리턴합니다.
        return what

class Computer(Contestant):
    def makeChoice(self):
        # 컴퓨터의 name을 받옵니다.
        name = self.getName()
        # rock, scissors, paper이 원소로 있는 리스트 중에서 랜덤으로 하나를 선택choice하도록 합니다. 
        li = ["rock","scissors","paper"]
        # 선택한 랜덤 원소를 rsp에 저장합니다. 
        rsp = random.choice(li)
        # 컴퓨터의 name과 rsp를 출력합니다. 
        print("{0} chooses {1}".format(name,rsp))
        # 컴퓨터가 고른 값을 리턴합니다. 
        return rsp

def playGames(h, c):
    # 가위 바위 보를 세번 반복 합니다. 
    for i in range(3):
        # 가위 바위 보 중 사람이 고른 값은 choiceH에 저장합니다.
        choiceH = h.makeChoice()
        # 가위 바위 보 중 컴퓨터가 고른 값은 choiceC에 저장합니다.
        choiceC = c.makeChoice()
        # 두 값이 같다면 비긴 것이므로 넘어갑니다.
        if choiceH == choiceC:
            pass
        #higher 함수를 이용하여 둘 중 누가 이겼는지 비교하고 이긴 사람의 점수를 incrementScore() 함수를 이용하여 1 높여줍니다. 
        elif higher(choiceH, choiceC):
            h.incrementScore()
        else:
            c.incrementScore()
        # 게임을 한번 시행할 때마다 사람의 점수, 컴퓨터의 점수를 프린트 합니다. 
        print(h.getName() + ":", h.getScore(),
            c.getName() + ":", c.getScore())
    # 세번의 게임이 다 끝난 후 사람과 컴퓨터의 점수가 같다면 비겼다고 출력하고 
    if(h.getScore()==c.getScore()):
        print("\nTIES")
    # 둘 중 점수가 더 큰 쪽이 있다면 그것의 이름을 대문자로 출력하고 WINS라는 메세지를 프린트 합니다. 
    elif(h.getScore()>c.getScore()):
        print("\n"+h.getName().upper()+" WINS")
    else:
        print("\n"+c.getName().upper()+" WINS")
# 가위 바위 보를 한번 시행할 때 누가 이겼는지 보여주는 함수 입니다. 
def higher(c1, c2):
    # c1 이 이기면 True를 리턴합니다. 
    if ((c1 == 'rock' and c2 == 'scissors') or
        (c1 == 'paper' and c2 == 'rock') or
        (c1 == 'scissors' and c2 == 'paper')):
        return True
    else:
        return False

def main():
    # 사람의 이름을 입력 받아 human에 저장합니다.
    human = str(input("Enter name of human: "))
    # 컴퓨터의 이름을 입력 받아 computer에 저장합니다.
    computer = str(input("Enter name of computer: "))
    # Contestant()에 입력 받은 사람 이름을 인자로 전달하여 객체를 만들고, 그 객체를 다시 Human()의 인자로 전달하여 생성한 Human 객체를 H에 저장합니다. 
    H = Human(Contestant(human))
    # Contestant()에 입력 받은 컴퓨터 이름을 인자로 전달하여 객체를 만들고, 그 객체를 다시 Computer()의 인자로 전달하여 생성한 Computer 객체를 C에 저장합니다. 
    C = Computer(Contestant(computer))
    # playGames 인자에 H와 C를 전달하여 게임이 일어나도록 합니다. 
    playGames(H,C)

main()
