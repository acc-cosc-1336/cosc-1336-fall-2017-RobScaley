from tkinter import Menu

class MainMenu(Menu):

    """Main menu for the Contoso Application"""

    def __init__(self, master=None, **kwargs):
        Menu.__init__(self, master, **kwargs)

        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label='Save Data', command=lambda: self.save_data)
        file_menu.add_command(label='Exit', command=self.quit)
        self.add_cascade(label='File', underline=0, menu=file_menu)

        data_menu = Menu(self, tearoff=0)
        data_menu.add_command(label='Courses', command=lambda: self.master.show_frame('CourseFrame'))
        data_menu.add_command(label='Enrollment', command=lambda: self.master.show_frame('EnrollmentFrame'))
        data_menu.add_command(label='Student', command=lambda: self.master.show_frame('StudentFrame'))
        self.add_cascade(label='Data', underline=0, menu=data_menu)

        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(label='About', command=lambda: self.master.show_frame("AboutFrame")) #frame is a key
        self.add_cascade(label='Help', underline=0, menu=help_menu)
