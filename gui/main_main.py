from tkinter import Menu

class MainMenu(Menu):

    """Main menu for the Contoso Application"""

    def __init__(self, master=None, **kwargs):
        Menu.__init__(self, master, **kwargs)

        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label='Save Data', command=lambda: self.save_data)
        file_menu.add_command(label='Exit', command=self.quit)
        self.add_cascade(label='File', underline=0, menu=file_menu)
