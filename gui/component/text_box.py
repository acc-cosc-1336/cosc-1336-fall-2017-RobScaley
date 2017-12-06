from tkinter import StringVar
from tkinter.ttk import Entry

from gui.component.listener import Listener

class TextBox(Entry):

    def __init__(self, master, value, data_source, index):
        Entry.__init__(self, master=master)
        self.index = index
        self.data_source = data_source
        self.value = StringVar()
        self.config(textvariable=self.value, width=15)

        self.value.set(value)
        self.data_source.addListener(Listener(self, "<<navigate_record>>",\
                                              lambda e: self.on_data_source_change()))
        
    def on_data_source_change(self):
        self.value.set(self.data_source.current_record()[self.index])
