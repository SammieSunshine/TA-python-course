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

import webbrowser

Summer =open("EOSSale.html","x")
Summer.close

Summer =open("EOSSale.html","w")
Summer.write("Stay tuned for our amazing summer Sale!")
Summer.close

Summer = open("EOSSale.html","r")
print(Summer.read())

