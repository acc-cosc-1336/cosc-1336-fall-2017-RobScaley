from tkinter import Tk, Frame
from gui.main_menu import MainMenu

from gui.frames.aboutframe import AboutFrame
from gui.frames.courseframe import CourseFrame
from gui.frames.enrollmentframe import EnrollmentFrame
from gui.frames.studentframe import StudentFrame

from data.school_db import SchoolDB
from data.school_initializer import SchoolInitializer

class ContosoApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, "Contoso University")

        self.school_db = SchoolDB(SchoolInitializer())

        self.menubar = MainMenu(self)
        self.config(menu=self.menubar)

        self.frames = {}
        self.__init_frames()

    def __init_frames(self):
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for frame in (AboutFrame, CourseFrame, EnrollmentFrame, StudentFrame):
            if frame.__name__ == "AboutFrame":
                current_frame = frame(container)
            else:
                current_frame = frame(container, self.school_db)
                
            self.frames[frame.__name__] = current_frame #sets current frame name as the key
            current_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        Tk.wm_title(self, 'Contoso University - ' + frame_name.replace('Frame', ''))
        frame.tkraise()

    def save_data(self):
        self.school_db.save_data()

app = ContosoApp()
app.geometry('640x400')
app.mainloop()
