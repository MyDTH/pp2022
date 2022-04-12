students = []
courses = []
marks = []

def numOfStudent():
    std_num = int(input("Enter the number of students in the class: "))
    return std_num

def studentInfo():
    std_id = input("Enter Student's ID: ")
    std_name = input("Enter Student's Name: ")
    std_dob = input("Enter Student's Date of Birth: ")
    print("--------------------")
    return std_id, std_name, std_dob

def numOfCourse():
    course_num = int(input("Enter the number of courses: "))
    return course_num

def courseInfo():
    course_id = input("Enter Course's ID: ")
    course_name = input("Enter Course's Name: ")
    print("--------------------")
    return course_id, course_name

def studentMarks(students, course):
    for i in range(len(students)):
        marks.append({course: {}})
        mark = float(input("Enter " + students[i].get("Name") + "'s mark:\n"))
        marks[i].update({course: mark})

def displayCourses():
    print("Course information:\n")
    for i in range(len(courses)):
        print("Course ID: " + courses[i].get("ID"))
        print("Course name: " + courses[i].get("Name"))
        print("--------------------")

def displayStudents():
    print("Student information:\n")
    for i in range(len(students)):
        print("Student ID: " + students[i].get("ID"))
        print("Student name: " + students[i].get("Name"))
        print("Student DoB: " + students[i].get("DoB"))
        print("--------------------")

def displayMarks():
    print("Student marks for this course:\n")
    for i in range(len(students)):
        print(students[i].get("Name") + "'s mark:")
        print(marks[i].get(select_course))
        print("\n")

if __name__ == "__main__":
    student_num = numOfStudent()
    print(student_num)
    for i in range(0, student_num):
        std_id, std_name, std_dob = studentInfo()
        students.append({"ID": std_id, "Name": std_name, "DoB": std_dob})

    course_num = numOfCourse()
    for i in range(0, course_num):
        course_id, course_name = courseInfo()
        courses.append({"ID": course_id, "Name": course_name})

    x = 'y'
    while x == 'y':
        print("---------------------")
        select_course_id = input("Select a course ID: ")
        for i in range(len(courses)):
            if courses[i].get("ID") == select_course_id:
                print("Course's Name: " + courses[i].get("Name") + "\n")
                studentMarks(students, courses[i].get("Name"))
        x = input("Do you want to select another course? y/n: ")
        print("--------------------")

    displayStudents()
    displayCourses()

    select_course = input("Select a Course's Name: ")
    displayMarks()