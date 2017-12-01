class Transcript:

    def __init__(self, enrollments):

        self.enrollments = enrollments

    def print_transcript(self, student):

        print("Student name: ", student.last_name + ', ' + student.first_name)
        sum_credit_points = 0
        sum_grade_points = 0
        print()
        print("Course", ' ' * 9, "Credit Hours", "Credit Points" , "Grade Points", "Letter Grade")

        for e in self.enrollments.values():

            if(student.student_id == e.student.student_id):
                credit_points = self.__get_credit_points(e.grade)
                grade_points = e.course.credit_hour * credit_points
                sum_credit_points += credit_points
                sum_grade_points += grade_points

                print(format(e.course.title, '15'),
                      format(e.course.credit_hour, '13'),
                      format(credit_points, '13'),
                      format(grade_points, '12'),
                      format(e.grade, '12'))

        if sum_credit_points > 0:
            print("GPA: ", sum_grade_points / sum_credit_points)

    def __get_credit_points(self, grade):

        credit_points = 0

        if grade == 'A':
            credit_points = 4
        elif grade == 'B':
            credit_points = 3
        elif grade == 'C':
            credit_points = 2
        elif grade == 'D':
            credit_points = 1

        return credit_points
