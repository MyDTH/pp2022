StudentList = []
StudentInfomation = {
    "Student's ID": None,
    "Name": None,
    "Date of Birth": None,
    "Course's ID": None,
    "Course's Name": None,
    "Course's Mark": None
}

def AddingStudents():
    NumOfStudents = int(input("Number of students in a class: "))
    for i in range(NumOfStudents):
        student = {
            "Student's ID": input("ID: "),
            "Name": input("Name: "),
            "Date of Birth": input("Date of Birth: "),
            "Course's ID": input("Course's ID: "),
            "Course's Name": input("Course's Name: "),
            "Course's Mark": input("Course's Mark: ")
        }
        StudentList.append(student)

def ListOfStudents():
    print("The number of students in a class is %s" % len(StudentList))
    for i in StudentList:
        print("{0}. Student infomation: ".format(i))

if __name__ == "__main__":
    AddingStudents()
    ListOfStudents()