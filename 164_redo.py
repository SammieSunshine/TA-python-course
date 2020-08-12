#
#
# Assignment 164(redo)
#
#
# Python ver. 3.8.5
#
# Author: Samantha Bilips
#
#
# Purpose: Use sqlite3 module reate database with a table of files with a ".txt" extension


import sqlite3





#creates db; connects to and holds connection
conn = sqlite3.connect('164_redo.db')

# Table with autoincremented primary key
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS table_Files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fname TEXT)')
    conn.commit()#won't work if not commited
conn.close()#close connecton


import sqlite3
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt', 'data.pdf' ,'myPhoto.jpg')

conn = sqlite3.connect('164_redo.db')
#insert .txt files into table

with conn:
    cur = conn.cursor()
    cur.execute(files)
    for files in fileList:
        if files.endswith(".txt"):
           insert files into table_Files
    conn.commit()
conn.close()


    
