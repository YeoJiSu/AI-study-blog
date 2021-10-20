def main():
    while(True):
        try:
            filename = input("Enter file name : ")
            infile = open(filename, 'r')
            num=int(infile.readline())
            print(1/num)
            break
        except FileNotFoundError as ex1:
            print(ex1)
        except ValueError as ex2:
            print(ex2)
main()