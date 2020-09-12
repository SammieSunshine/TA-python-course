#
#
# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
#
# Challenge info:
# For this assignment, you will write a script that creates a GUI.
# REQUIREMENTS:
#   Your script will need to use Python 3 and the Tkinter module.
#   Your script will need to re-create an exact copy of a GUI from the supplied
#   image at the bottom of page 248



from tkinter import *



class FileCheck(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,185))
        self.master.title('Check files')
        self.master.config(bg='#efefef')

        self.varSpace1 = StringVar()
        self.varSpace2 = StringVar()
        self.varCheck = StringVar()

        def Browse1(self):
            Space1 = self.varSpace1.get()

        def Browse2(self):
            Space2 = self.varSpace2.get()

        def checkFiles(self):
            Space1= self.varCheck.get()

        def closeProgram(self):
            self.master.destroy()

        self.browse1 = Button(self.master, text= 'Browse...', width=12, height=1, command=Browse1)
        self.browse1.grid(row=0, column=0, padx=(15,0), pady=(50,0), sticky=NW)
        
        self.browse2 = Button(self.master, text= 'Browse...',width=12, height=1, command=Browse2)
        self.browse2.grid(row=1, column=0, padx=(15,0), pady=(10,0), sticky=NW)

        self.checkfiles = Button(self.master, text= 'Check for files...', width=12, height=2, command=checkFiles)
        self.checkfiles.grid(row=2, column=0, padx=(15,0), pady=(10,0), sticky=NW)
        
        self.closeProgram = Button(self.master, text= 'Close Program', width=12, height=2, command=closeProgram)
        self.closeProgram.grid(row=2, column=3, padx=(10,0), pady=10, sticky=SE)

        self.txt1=Entry(self.master, text='', font=('sans serif',16),width=28,fg='black',bg='white')
        self.txt1.grid(row=0,column=3, padx=(31,0), pady=(50,1), sticky=NW)

        self.txt2=Entry(self.master, text='', font=('sans serif',16), width=28,fg='black',bg='white')
        self.txt2.grid(row=1,column=3, padx=(31,0), pady=(10,1), sticky=NW)

      
            



if __name__=="__main__":
    root=Tk()
    App = FileCheck(root)
    root.mainloop()
