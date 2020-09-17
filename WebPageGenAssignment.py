#
#
# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
#
# Assignment:
#
#  WEB PAGE GENERATOR ASSIGNMENT PART ONE
#  You’ve been asked by users for a tool that can automatically create a basic HTML web page.
#  The page is very simple. It will simply have the text "Stay tuned for our amazing summer sale!" on the page.
#  Your task is to create a Python script that will automatically create the .html file needed.
# Part 2: 
# Now that you have created a tool that can automatically create a basic HTML web page, the content on the page is hard-coded as "Stay tuned for our amazing summer sale!"
# Users have now asked you to create an option for them to set the body of the text themselves.
# Your task is to create a GUI with Tkinter that will enable the users to set the body text for a newly-created web page. There should also be a control in the GUI that initiates the process of making the new web page.
# Set a new body text of your choice.
# The GUI should open the html file in a new tab within your browser that displays the newly added text from the user.


import tkinter as tk
import webbrowser
import html
import os


#Web Generator frame
window = tk.Tk()

   
frame = tk.Frame(
    master = window,
    width = 100,
    height = 100,
    bg = "Silver")
frame.pack()

#Application creation
WebGen = App()

#Window manager method calls
WebGen.master.title('Web Page Generator')
WebGen.master.resizable(width=True, height=True)
WebGen.master.config(bg="Silver")

class  Client(WebGen,WPhtml):
    WebLabel = tk.Label(text="Enter Body of text here")
    WebBody = tk.Entry()

    def ClientEntry(WebGen,WPhtml):
        WebLabel.pack()
        WebBody.pack()
        
#new web page creation




# messagebox - tells client that their page settings have been saved
messagebox.showinfo(message='Your Web Page has been updated!')


window.mainloop()
