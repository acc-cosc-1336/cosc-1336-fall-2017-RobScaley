class Student:
    def __init__(self, student_id, first_name, last_name, enroll_date):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.enroll_date = enroll_date

    def __repr__(self):
        return "student id: {}, student: {} {}".format(self.student_id, self.first_name, self.last_name)

class Course:
    def __init__(self, course_id, title, credit_hour):
        self.course_id = course_id
        self.title = title
        self.credit_hour = credit_hour

    def __repr__(self):
        return "course id: {}, course: {}".format(self.course_id, self.title)

class Enrollment:
    def __init__(self, enroll_id, student, course):
        self.enroll_id = enroll_id
        self.student = student
        self.course = course
        self.grade = "N/A"

    def set_grade(self, grade):
        self.grade = grade

    def __repr__(self):
        return "id: {}, student: {}, course: {}, grade: {}".format(self.enroll_id,\
                                                       self.student.first_name + ' ' + self.student.last_name,\
                                                       self.course.title,\
                                                                   self.grade)

class Gradebook:
    def __init__(self):
        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexander", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s


        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3)
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4)
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4)
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3)
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4)
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

    def add_student(self):
        s_id = int(input("Please enter a student id: "))
        first_name = input("Please enter the student's first name: ")
        last_name = input("Please enter the student's last name: ")
        enroll_date = input("Please enter the date of enrollment: ")
        s = Student(s_id, first_name, last_name, enroll_date)
        self.students[s.student_id] = s

    def add_enrollment(self):
        s = input("Please enter the student id of the student you'd like to enroll: ")

        c_id = input("Please enter the course id of the class you'd like to add: ")
        enroll_id = int(s + c_id)
        enrollment = Enrollment(enroll_id, self.students[int(s)], self.courses[int(c_id)])
        
        self.enrollments[enroll_id] = enrollment

class Main:
    def __init__(self):
        gradebook = Gradebook()
        
        keep_going1 = input("Would you like to add a student? (y/n): ").lower()
        while keep_going1 == 'y':
            gradebook.add_student()
            keep_going1 = input("Would you like to add another student? (y/n): ").lower()
        print()

        keep_going2 = input("Would you like to add an enrollment? (y/n): ").lower()
        while keep_going2 == 'y':
            gradebook.add_enrollment()
            keep_going2 = input("Would you like to add another enrollment? (y/n): ").lower()
        print()
        
        keep_going3 = input("Would you like to update a grade? {y/n): ").lower()
        while keep_going3 == 'y':
            e_id = int(input("Please enter an enrollment id for the grade you'd like to add: "))
            grade = input("What grade did the student earn? ").upper()
            gradebook.enrollments[e_id].set_grade(grade)
            keep_going3 = input("Would you like to change another grade? (y/n): ")
        print()

        print("\nPrinting enrollment list:\n")
        for i in gradebook.enrollments:
            print(gradebook.enrollments[i])
        
main = Main()




