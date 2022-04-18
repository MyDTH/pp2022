class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("Student's ID: " + self.id)
        print("Student's Name: " + self.name)
        print("Student's DoB: " + self.dob)
        print("--------------------")

    def displayMark(self, course):
        print(self.name + "'s mark: " + str(self.marks.get(course)))


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def displayCourse(self):
        print("Course's ID: " + self.id)
        print("Course's Name: " + self.name)
        print("--------------------")


def numOfStudent():
    while True:
        try:
            std_num = int(input("Enter number of students in the class: "))
            print("--------------------")
            return std_num
        except ValueError:
            print("Invalid number.")


def studentInfo():
    std_id = input("Enter student's ID: ")
    std_name = input("Enter student's name: ")
    std_dob = input("Enter student's date of birth: ")
    print("--------------------")
    return std_id, std_name, std_dob


def numOfCourse():
    while True:
        try:
            course_num = int(input("Enter number of courses: "))
            print("--------------------")
            return course_num
        except ValueError:
            print("Err: Invalid number.")


def courseInfo():
    course_id = input("Enter course's ID: ")
    course_name = input("Enter course's name: ")
    print("--------------------")
    return course_id, course_name


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Err: Invalid ID")


if __name__ == "__main__":
    students = []
    courses = []

    student_num = numOfStudent()
    print(student_num)
    for i in range(0, student_num):
        id, name, dob = studentInfo()
        students.append(Student(id, name, dob))

    course_num = numOfCourse()
    for i in range(0, course_num):
        id, name = courseInfo()
        courses.append(Course(id, name))

    print("Display students' information:\n")
    for student in students:
        student.displayStudent()

    print("Display courses' information:\n")
    for course in courses:
        course.displayCourse()

    x = 'y'
    while x == 'y':
        select_course_id = input("Select a course ID: ")
        select_course = findCourseName(courses, select_course_id)
        print("Course name: " + select_course + "\n")
        for student in students:
            mark = input("Enter " + student.name + "'s mark: ")
            student.set_mark(select_course, mark)
        x = input("Do you want to select another course? y/n: ")
        print("-------")

    select_course_id = input("Select a displayed course's ID: ")
    select_course = findCourseName(courses, select_course_id)
    print(f"Display students' marks of course {select_course}:\n")
    for student in students:
        student.displayMark(select_course)