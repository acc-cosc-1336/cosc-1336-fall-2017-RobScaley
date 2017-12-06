class EnrollmentDictionary:

    def __init__(self, enrollments):
        self.dictionary = {}

        for key in enrollments:
            enrollment = enrollments[key]
            self.dictionary[key] = [key, enrollment.course.title, enrollment.student.first_name + " " + \
                                            enrollment.student.last_name, enrollment.grade]


        
