from model.transcript import Transcript
from data.school_db import SchoolDB
from data.school_initializer import SchoolInitializer

class Gradebook:

    def __init__(self, school_db):

        self.school_db = school_db
        self.enrollments = school_db.enrollments
        self.students = school_db.school_initializer.students

    def main(self):

        choice = ''

        while choice.lower() != 'e':
            print()
            choice = self.__display_menu()

            if choice == '1':

                enroll_key = int(input("Enter enroll key"))

                if enroll_key in self.enrollments:
                    enroll = self.enrollments.get(enroll_key)

                    grade = input("Enter grade: ")
                    enroll.grade = grade

                else:
                    print("Key doesn't exist")

            elif choice == '2':

                student_id = int(input("Enter student id: "))

                if student_id in self.students:
                    transcript = Transcript(self.enrollments)
                    student = self.students.get(student_id)
                    transcript.print_transcript(student)

            elif choice == '3':

                for enrollment in self.enrollments.values():
                    enrollment.print_record()

            elif choice == '4':

                self.school_db.save_data()

            print()

    def __display_menu(self):

        print("Academic Main Menu")
        print()
        print("1) Update Grade")
        print("2) Print Student GPA")
        print("3) Print All Enrollments")
        print("4) Save Data")
        print()
        return input("Enter 1, 2, 3, or e to exit: ")

db = SchoolDB(SchoolInitializer())
gradebook = Gradebook(db)
gradebook.main()
