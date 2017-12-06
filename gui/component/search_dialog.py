from tkinter import Toplevel, StringVar, Label, Entry, Button

class SearchDialog(Toplevel):
    def __init__(self, parent, prompt):
        Toplevel.__init__(self, parent)

        self.wm_title("Search Dialog")
        self.var = StringVar()
        self.entry = Entry(self, textvariable=self.var)

        self.label = Label(self, text=prompt)
        self.ok_button = Button(self, text="OK", command=self.on_ok)

        self.label.pack(side='top', fill='x')
        self.entry.pack(side='top', fill='x')
        self.ok_button.pack(side='right')
        self.entry.bind("<Return>", self.on_ok)

    def on_ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()
