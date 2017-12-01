from model.person import Person

class Professor(Person):

    def __init__(self, professor_id, first_name, last_name, hire_date):

        Person.__init__(self, first_name, last_name)
        self.professor_id = professor_id
        self.hire_date = hire_date
