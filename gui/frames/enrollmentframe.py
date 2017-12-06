from tkinter import Frame, Label

from gui.component.datagrid import DataGrid
from gui.component.enrollmentdictionary import EnrollmentDictionary
from gui.component.datasource import DataSource
from gui.component.listener import Listener
from gui.component.navigation_bar import NavigationBar
from gui.component.search_dialog import SearchDialog
from gui.component.text_box import TextBox

class EnrollmentFrame(Frame):
    """Frame container for Enrollment screen"""
    
    def __init__(self, parent, school_db):
        Frame.__init__(self, parent)

        self.school_db = school_db
        self.enrollDict = EnrollmentDictionary(self.school_db.enrollments)
        self.data_source = DataSource(self, self.enrollDict)

        self.init_form()

        self.data_source.addListener(Listener(self, "<<update_record>>",
                                              lambda e: self.on_update()))

    def init_form(self):

        Label(self, text="Id").grid(row=0, column=0, sticky="w")
        self.id_text_box = TextBox(self, "", self.data_source, 0)
        self.id_text_box.grid(row=0, column=0, sticky="e")

        Label(self, text="Student").grid(row=1, column=0, sticky="w")
        self.student_text_box = TextBox(self, "", self.data_source, 2)
        self.student_text_box.grid(row=1, column=0, sticky="e")

        Label(self, text="Course").grid(row=2, column=0, sticky="w")
        self.course_text_box = TextBox(self, "", self.data_source, 1)
        self.course_text_box.grid(row=2, column=0, sticky="e")

        Label(self, text="Grade").grid(row=3, column=0, sticky="w")
        self.grade_text_box = TextBox(self, "", self.data_source, 3)
        self.grade_text_box.grid(row=3, column=0, sticky="e")
        
        navigation = NavigationBar(self, self.data_source)
        navigation.grid(row=4, columnspan=3)
        
        self.data_grid = DataGrid(self, ['Id', 'Course', 'Student', 'Grade'],
                                  self.data_source)

        self.data_grid.grid(row=5, columnspan=3, sticky="nswe")

    def on_search(self):
        search_string = SearchDialog(self, "Enter enroll Id: ").show()

        enrollment_list = self.data_source[int(search_string)]
        self.data_source.set_current_record(enrollment_list[0])
        self.data_grid.on_set_record(enrollment_list[0])
                                     
    def on_update(self):
        enrollment_list = self.data_source.data[int(self.id_text_box.value.get())]
        enrollment_list[3] = self.grade_text_box.value.get()

        enrollment = self.school_db.school_initializer.enrollments[enrollment_list[0]]
        enrollment.grade = self.grade_text_box.value.get()

        self.data_source.update_record(enrollment_list)
        self.data_grid.on_update_record(enrollment_list)
