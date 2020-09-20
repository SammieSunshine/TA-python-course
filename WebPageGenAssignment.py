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

#get text from the entry widget and assign it to the variable.
#open the HTML file for writing(get a file object as a variable)
#create a variable that holds a string of HTML code concatenating the text from the entry widget in
#write the variable from step 3 to the html file
#close the html file
#open the html file in the web browser

import tkinter as tk
import webbrowser
import html


#root main callback
root = tk.Tk()

#Window manager method calls, page title, and window appearance
root.master.title('Web Page Generator')
root.master.config(bg="Silver",
                     font = 'san serif',) 

#Label to let user know where body of text can be enter 
WebLabel = tk.Label(root,text='Enter new content below',font=('calibre', 11, 'bold'))
#User input goes here in entry
ContentEntry = tk.Entry(root,       
                   textvariable= WPTxt,    
                   font=('sans serif', 14, 'bold')
                    
#retrieves/holds user input
WPContent = ContentEntry.get()
                        
# opens html file object; 'w' allows user input to override Page content
WPhtmlFile = open("GenSelfService.html", "w")
                        
#create a variable that holds HTML code with Entry widget concatenated inside                   
WPhtml = '<!DOCTYPE html>\n <html lang="en">\n <head>\n <meta charset="UTF-8">\n <title>Web Page </title>\n <body>'+ ContentEntry + '</body>\n</head>\n </html>'
    
#Write variable from step 3(above)to html file
WPhtmlFile.write(WPhtml)                      
                 

#Submit button to send new content to page
SubmitContent = tk.Button(root,text='Submit Edited/New Content', command =submit)

#close File
WPhtmlFile.close

#Open html file in web browser
webbrowser.open_new_tab(WPhtmlFile)
                        
