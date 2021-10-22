# USPres 중 VPres 이였던 사람을 new에다가 붙여넣기 
infile1 = open("VPres.txt",'r')
infile2 = open("USPres.txt",'r')
outfile = open("new.txt",'w')

Pres = [line.rstrip() for line in infile1]
for person in infile2:
    if person.rstrip() in Pres: # 여기서 person.rstrip() 반드시 붙여야 해 !!!!
        outfile.write(person)

infile1.close()
infile2.close()
outfile.close()  