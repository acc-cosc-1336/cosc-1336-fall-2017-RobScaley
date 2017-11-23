class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    def __init__(self, student_id, first_name, last_name, enroll_date):
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.enroll_date = enroll_date

    def __repr__(self):
        return "student id: {}, student: {} {}".format(self.student_id, self.first_name, self.last_name)

class Professor(Person):
    def __init__(self, professor_id, first_name, last_name, hire_date):
        Person.__init__(self, first_name, last_name)
        self.professor_id = professor_id
        self.hire_date = hire_date

    def __repr__(self):
        return "student id: {}, professor: {} {}".format(self.professor_id, self.first_name, self.last_name)

class Course:
    def __init__(self, course_id, title, credit_hour, professor):
        self.course_id = course_id
        self.title = title
        self.credit_hour = credit_hour
        self.professor = professor

    def __repr__(self):
        return "course id: {}, course: {}".format(self.course_id, self.title)

class Enrollment:
    def __init__(self, enroll_id, student, course, letter_grade):
        self.enroll_id = enroll_id
        self.student = student
        self.course = course
        self.grade = letter_grade.upper()
        self.grade_number = self.convert_grade()

    def set_grade(self, grade):
        self.grade = grade

    def convert_grade(self):
        if self.grade == 'A':
            return 4
        elif self.grade == 'B':
            return 3
        elif self.grade == 'C':
            return 2
        elif self.grade == 'D':
            return 1
        elif self.grade == 'F':
            return 0
        elif self.grade == 'I' or self.grade == 'W':
            return ''

    def __repr__(self):
        return "id: {}, student: {}, course: {}, grade: {}".format(self.enroll_id,\
                                                       self.student.first_name + ' ' + self.student.last_name,\
                                                       self.course.title,\
                                                                   self.grade)
class Transcript:
    def __init__(self, enroll_dict, students):
        self.enroll_dict = enroll_dict
        self.students = students

    def print_transcript(self, student_id):
        total_credit_hours = 0
        total_grade_points = 0
        print("Name: {} {}".format(self.students[student_id].first_name,\
                                   self.students[student_id].last_name))
        print()
        print("Class\t\tCredit Hours\tCredit Points\tGrade Points\tGrade")
        
        for i, v in self.enroll_dict.items():
            if str(i)[:1] == str(student_id):
                if isinstance(v.grade_number, int):
                    grade_points = v.grade_number * v.course.credit_hour
                    total_grade_points += grade_points
                    total_credit_hours += v.course.credit_hour
                else:
                    grade_points = ""
                
                print("{}\t\t{}\t\t{}\t\t{}\t{}".format(v.course.title, v.course.credit_hour,\
                                          v.grade_number, grade_points, v.grade))
        print('-' * 70)
        print('\t\t\t{}\t\t\t\t{}'.format(total_credit_hours, total_grade_points))
        print("GPA:", round(total_grade_points/total_credit_hours, 2))

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

        self.professors = {}

        #professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11") 
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06") 
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01") 
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12") 
        self.professors[p.professor_id] = p

        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3, self.professors[2])
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4, self.professors[3])
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041], 'I')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045], 'B')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141], 'C')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041], 'B')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050], 'F')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022], 'W')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021], 'C')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141], 'C')
        self.enrollments[enroll_id] = enrollment

        self.transcript = Transcript(self.enrollments, self.students)

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

##class Main:
##    def __init__(self):
##        gradebook = Gradebook()
##        
##        keep_going1 = input("Would you like to add a student? (y/n): ").lower()
##        while keep_going1 == 'y':
##            gradebook.add_student()
##            keep_going1 = input("Would you like to add another student? (y/n): ").lower()
##        print()
##
##        keep_going2 = input("Would you like to add an enrollment? (y/n): ").lower()
##        while keep_going2 == 'y':
##            gradebook.add_enrollment()
##            keep_going2 = input("Would you like to add another enrollment? (y/n): ").lower()
##        print()
##        
##        keep_going3 = input("Would you like to update a grade? {y/n): ").lower()
##        while keep_going3 == 'y':
##            e_id = int(input("Please enter an enrollment id for the grade you'd like to add: "))
##            grade = input("What grade did the student earn? ").upper()
##            gradebook.enrollments[e_id].set_grade(grade)
##            keep_going3 = input("Would you like to change another grade? (y/n): ")
##        print()
##
##        print("\nPrinting enrollment list:\n")
##        for i in gradebook.enrollments:
##            print(gradebook.enrollments[i])
##        
##main = Main()

class Main:
    def __init__(self):
        gradebook = Gradebook()
        keep_going = 'y'

        while keep_going == 'y':
            student = int(input("Enter student id: "))
            if student in gradebook.students:
                gradebook.transcript.print_transcript(student)
                keep_going = input("Would you like to enter another student id? (y/n): ")
            else:
                print("Invalid student id.")
                input("Press enter to continue.")

main = Main()

