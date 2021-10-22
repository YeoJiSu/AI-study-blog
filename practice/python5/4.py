# os를 이용하여 파일 관리 
import os
# 파일 없애기 
#os.remove("new.txt")
# 파일 이름 변경하기
#os.rename("new.txt","old.txt") 
#os.rename("old.txt","new.txt")

# 없는 파일 만들기 
if os.path.isfile("ABC.txt"):
    print("Already exists")
else : 
    outfile = open("ABC.txt",'w')
    outfile.writelines(["helpp\n","isji\n"])
