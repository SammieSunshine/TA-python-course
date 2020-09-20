import tkinter
from tkinter import *
import tkinter as tk


#Main GUI frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("Web Page Generator")

        #grids can be different dimensions
        self.labelTxt = Label(text = "Enter new content below", font=("Arial", 12))
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))

        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)

        self.btnSubmit = Button(self.master, text="Submit", width=12, height=1, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.master.columnconfigure(1,weight=1)

    #Custom GUI function for button commands 
    def customEntry(self):
        #retrieves/holds user input
        txtEntryVariable = self.txtEntry.get()

        
        #An action for this template to do smething would go below here
 
        
       
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
