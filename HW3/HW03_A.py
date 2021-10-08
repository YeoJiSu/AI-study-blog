def readSetFromFile():
    # Names.txt 파일을 열어서 읽음 
    infile = open("Names.txt",'r')
    # 한줄씩 읽어와 list 안에 추가함 
    myList = [line.rstrip() for line in infile ]
    # 파일을 닫음 
    infile.close()
    # list를 set으로 변환하여 return 함 
    mySet= set(myList)
    return mySet
    
def inputName():
    # 파일안에 넣을 이름을 입력받고 그 값을 리턴함. 
    name = input("Enter a first name to be included: ")
    return name

def insertSet(mySet, name):
    # 만약 입력받은 이름이 set 안에 없다면 set 안에 name을 추가함. 
    if name not in mySet:
        print("Mango is added in Names.txt")
        mySet.add(name)
    else: # set 안에 이미 이름이 존재한다면 추가하지 않음 .
        print("Mango is already in Names.txt")
    # mySet을 알파벳순으로 다시 정렬하여 리턴함 .
    return sorted(mySet)
    
def writeToFile(modifiedSet):
    # Names.txt 파일을 열어서 작성함 
    outfile = open("Names.txt",'w')
    # set 안의 값들을 하나씩 적고 줄바꿈 하여 작성함. 
    for fruit in modifiedSet:
        outfile.write(fruit+"\n")
    # set안의 원소들을 다 적으면 파일 닫음 .
    outfile.close()

def main():
    # 파일 값을 set으로 return한 함수를 이용해 set을 mySet에 저장함 
    mySet = readSetFromFile()
    # 파일에 추가할 새 이름을 입력받는 함수를 불러와 그 이름을 name에 저장함 .
    name = inputName()
    # mySet에 name이 있는지 검사 없다면 name을 넣어주고 그 set을 리턴하는 함수를 불러와 변수에 저장
    modifiedSet = insertSet(mySet, name)
    # 그 set을 다시 파일에 쓰는 함수를 불러옴 .
    writeToFile(modifiedSet)

main()
