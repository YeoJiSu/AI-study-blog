import random
NUMBER_OF_TRIALS = 10000

def matchTwoDecks():
    # 난수 생성기를 초기화한다. 
    random.seed()
    # 일치하는 횟수를 numMatches 변수에 저장하고 0으로 초기화 한다. 
    numMatches = 0
    # 1부터 52까지의 정수 무작위로 생성 
    deck1= random.randint(1,52)
    deck2= random.randint(1,52)
    # 두 수가 같다면 numMatches 변수를 1로 바꾸고 리턴한다. 
    if (deck1==deck2):numMatches =1
    return numMatches

def main():
    totalMatches = 0
    for i in range(NUMBER_OF_TRIALS):
        totalMatches += matchTwoDecks()
    averageMatches = totalMatches / NUMBER_OF_TRIALS
    # 기존 스켈레톤 코드의 프린트 부분이 에러가 나서 약간 수정했습니다.
    print("Average number of matched cards: {:.3f}".format(averageMatches))

main()
