from tkinter import LEFT
from tkinter.ttk import Frame, Button

class NavigationBar(Frame):

    def __init__(self, parent, data_source):
        Frame.__init__(self, parent)

        self.data_source = data_source
        self.init_form()

    def init_form(self):
        nextButton = Button(self, text="Next     ", command=self.on_next)
        updateButton = Button(self, text="Update     ", command=self.on_update)
        deleteButton = Button(self, text="Delete     ", command=self.on_delete)
        previousButton = Button(self, text="Previous     ", command=self.on_previous)
        searchButton = Button(self, text="Search     ", command=self.master.on_search)

        nextButton.pack(side=LEFT)
        previousButton.pack(side=LEFT)
        updateButton.pack(side=LEFT)
        deleteButton.pack(side=LEFT)
        searchButton.pack(side=LEFT)

    def on_next(self):
        self.data_source.next_record()
    
    def on_update(self):
        self.data_source.request_update()
        
    def on_delete(self):
        pass
    
    def on_previous(self):
        self.data_source.previous_record()
