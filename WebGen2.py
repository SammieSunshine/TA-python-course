import tkinter
from tkinter import *
import webbrowser
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("Web Page Generator")

        self.labelTxt = Label(text = "Enter new content below", font=("Arial", 12))
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))

        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)

        self.btnSubmit = Button(self.master, text="Submit", width=12, height=1, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.master.columnconfigure(1,weight=1)

    def customEntry(self):
        #retrieves/holds user input
        WPContent = self.txtEntry.get()
        # opens html file object; 'w' allows user input to override Page content
        WPhtmlFile = open("GenSelfService.html", "w")
                            
        #create a variable that holds HTML code with Entry widget concatenated inside                   
        WPhtml = '<!DOCTYPE html>\n <html lang="en">\n <head>\n <meta charset="UTF-8">\n <title>Web Page </title>\n <body>'+ WPContent + '</body>\n</head>\n </html>'

        #Write variable from step 3(above)to html file
        WPhtmlFile.write(WPhtml)

        #close File
        WPhtmlFile.close()
        

        webbrowser.open_new_tab("GenSelfService.html")           

        
       
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
