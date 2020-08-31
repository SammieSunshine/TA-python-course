#
#
#   Python Version: 3.8.5
#
#   Author: Samantha Billips
#

#   Create a database table in RAM named Roster that includes the fields
#   'Name', 'Species', and 'IQ'

import sqlite3

#   Variable of info to be plugged into table
RosterValues = (('Jean-Baptiste Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),('Ak\'not','Mangalore',-5))

with sqlite3.connect(":memory:")as connection:#RAM database temp
    c = connection.cursor()
# create variable for information to be inserted
    c.execute("DROP TABLE IF EXISTS Roster")#Just in case
    c.execute("CREATE TABLE IF NOT EXISTS Roster( Name TEXT, Species TEXT, IQ INT)")
# insert placeholder '?' for values; connected to variable
    c.executemany("INSERT INTO Roster (Name,Species,IQ)  VALUES (?,?,?)",RosterValues)
# Update Korben Dallas' species to Human
    c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'")
# Display names and IQs of everyone in the table who is classified as Human
    c.execute("SELECT Name,IQ  FROM Roster WHERE Species ='Human'")
    for row in c.fetchall():
        print(row)
