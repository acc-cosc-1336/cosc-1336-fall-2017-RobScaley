
class Enrollment:

    def __init__(self, enroll_id, student, course):

        self.enroll_id = enroll_id
        self.student = student
        self.course = course
        self.grade = ''

    def print_record(self):

        print(self.enroll_id,
              format(self.student.last_name, '15'),
              format(self.student.first_name, '15'),
              format(self.course.title, '20'),
              format(self.grade, '5'))



