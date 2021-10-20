import student
def main():
    # students and grades
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
            st = student.LGstudent(name, midterm, final)
        else:
            st = student.PFstudent(name, midterm, final) 
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ") 
        carryOn = carryOn.upper()
    return listOfStudents
def displayResults(listOfStudents): 
    print("\nNAME\tGRADE")
    # Sort students by name.
    listOfStudents.sort(key = lambda x: x.getName()) 
    for pupil in listOfStudents:
        print(pupil) 
main()