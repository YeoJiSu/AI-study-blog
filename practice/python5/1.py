# 1.for line in infile: ->  각각의 라인을 하나씩 읽는 것임 
# rstrip() -> 라인읽었을 때 오른쪽 빈공간을 다 제거해줌 
# 2.[] =>  바로 리스트를 구성할 수 있음 
# 3. readline() 
# 반드시 이거 해볼 것 
def printTXT():
    while (1):
        a = input("filename: ")
        try : 
            infile = open(a, 'r')
            for line in infile:
                print(line.rstrip())
            infile.close()
            break;
        except FileNotFoundError as ex1:
            print(ex1)

def printList(filename):
    infile = open(filename, 'r')
    list = [line.rstrip() for line in infile]
    infile.close()
    return list

def printFile(filename):
    infile = open(filename,'r')
    line = infile.readline()
    while line !="" :
        print(line.rstrip())
        line = infile.readline()   
    #print(infile.readline())
    infile.close()
    


def main():
    #printTXT()
    #print(printList("FirstPresidents.txt"))
    printFile("FirstPresidents.txt")
main()