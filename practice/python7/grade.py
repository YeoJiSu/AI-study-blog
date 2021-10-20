# grade class와 lists of objects 결합 
class Grade:
    def __init__(self, name, mid, final ):
        self.name = name
        self.mid = mid
        self.final = final
    def setName(self,name):
        self.name = name
    def setMid(self, mid):
        self.mid = mid
    def setFinal(self, final):
        self.final = final
    def getName(self):
        return self.name 
    def getMid(self):
        return self.mid
    def getFinal(self):
        return self.final
    def grade(self):
        grade = (self.mid+self.final)/2.0
        if grade>=90 : return "A"
        elif grade >=80 : return "B"
        elif grade >=70 : return "C"
        elif grade >=60 : return "D"
        elif grade >=50 : return "E"
        else: return "F"
    def __str__(self):
        my_str = "Name: {0} | Mid: {1} | Final: {2}\nGRADE: {3}\n".format(self.name, self.mid, self.final,self.grade())
        return my_str
def main():
    my_list = []
    keep = "Y"
    while (keep =="Y"):
        name = input("what is your name?: ")
        mid = int(input("mid-term exam: "))
        final = int(input("final-term exam: "))
        grade = Grade(name,mid,final)
        my_list.append(grade)
        keep = input("Continue? Y/N: ")
        keep = keep.upper()
    print("\n-------------Student's GRADE---------------\n")
    for g in my_list:
        print(g)
main()