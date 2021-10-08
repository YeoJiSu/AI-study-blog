def populateDictionary():
    # Units.txt 파일을 열어서 읽음 
    infile = open("Units.txt",'r')
    # 한줄씩 읽는데 comma를 기준으로 자른 list를 또 list안에 추가하여 변수 myList에 저장함. 
    myList = [line.rstrip().split(',') for line in infile ]
    infile.close()
    # 2차원 리스트 형태를 가진 myList를 dictionary로 변환하여 변수 dic에 저장함. 
    dic = dict(myList)
    # dic의 value의 자료형이 string인데 float으로 바꿔야하므로 map을 이용하여 타입을 변환함.
    # dic의 key와 타입 변환한 value를 zip에 넣은 뒤 dict를 사용하여 다시 dictionary를 만들어 mydic에 저장.  
    mydic = dict(zip(dic.keys(),list(map(float,dic.values()))))
    # mydic을 리턴함 
    return mydic

def getInput():
    # 변환할 unit, 변환될 unit, 그리고 길이를 입력 받고 세가지 값 모두 리턴함.
    orig = input("Unit to convert from: ")
    dest = input("Unit to convert to: ")
    # 변환할 unit을 format을 이용해 문자열안에 나타냄. 
    length = int(input("Enter length in {0}: ".format(orig)))
    return orig, dest, length;

def main():
    # txt 파일을 읽고 dictionary로 변환하는 함수를 불러와 feet에 dictionary를 저장함 
    feet = populateDictionary()
    # getInput 함수를 불러와 orig, dest,length 함수에 각각 return 값을 저장함 
    orig, dest, length = getInput()
    # orig, dest 키를 dictionary에 넣어 value 값을 가져와 계산하고 그 값을 ans에 저장
    ans = length * feet[orig] / feet[dest]
    # format 형식에 맞게 리턴함 
    print("Length in {0}s: {1:,.4f}".format(dest, ans))
main()
