# new.txt 파일에 USPres 내용 읽어와 작성하기 
infile = open("USPres.txt" , 'r')
#myList = [line.rstrip() for line in infile]
List = [line1 for line1 in infile]
infile.close()

outfile = open("new.txt", 'w') # w 대신 a 적으면 원래 파일에 적혀있는 내용 살아 있음 
List.sort()
# for i in range(len(List)):
#     outfile.write(List[i])
outfile.writelines(List)
outfile.close()

fl = open("new.txt",'r')
for line in fl:
    print(line.rstrip())
fl.close()

