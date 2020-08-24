#
#
#   Python ver: 3.8.5
#
#   Author: Samantha Bililps
#
#   Purpose: Phonebook Demo, OOP demonstration, Tkinter GUI module,
#               using Tkinter Parent and Child relationships
#
#   Tested OS: Code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Be sure to import our other modules
#So we can have access to them

import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocal method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" in windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a seperate module
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        #This is the menu that will appear at the top of the window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff= 0)
        filemenu.add_seperator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) #defines particular drop down column; tearoff=0 means do not seperate from menubar
        helpmenu.add_seperator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_seperator()
        helpmenu.add_command(label="About this Phonebook Demo") #add_command is a child menu bar item of the add_cascade parent item
        menubar.add_cascade(label="Help", menu=helpmenu) #add_cascade = parent menubar item(visible heading)


        self.master.config(menu=menubar, borderwidth='1')

if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
