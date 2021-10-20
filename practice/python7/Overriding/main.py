def main():
    # Students and grades
    listOfStudents = obtainListOfStudents() 
    displayResults(listOfStudents)
    
def obtainListOfStudents(): 
    listOfStudents = [] 
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")  
        midterm = float(input("Enter grade on midterm: ")) 
        final = float(input("Enter grade on final: ")) 
        category = input("Enter category (LG or PF): ") 
        if category.upper() == "LG":
            st = LGstudent(name, midterm, final) 
        else:
            st = PFstudent(name, midterm, final) 
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ") 
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents): 
    print("\nNAME\tGRADE")
    listOfStudents.sort(key = lambda x: x.getName()) 
    for pupil in listOfStudents:
        print(pupil)
        
class LGstudent:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name 
        self._midterm = midterm 
        self._final = final
    def setName(self, name): 
        self._name = name
    def setMidterm(self, midterm): 
        self._midterm = midterm
    def setFinal(self, final): 
        self._final = final
    def getName(self): 
        return self._name
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2) 
        if average >= 90:
            return "A"
        elif average >= 80: return "B"
        elif average >= 70: return "C"
        elif average >= 60: return "D"
        else:
            return "F"
    def __str__(self): 
        return self._name +"\t" + self.calcSemGrade()

class PFstudent(LGstudent): 
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2) 
        if average >= 60:
            return "Pass" 
        else:
            return "Fail"

main()
