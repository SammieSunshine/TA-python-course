#Datetime test
#
#
# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
#
# Challenge Info:
# The Portland-based Company you work for just opened two new branches.
# One is in NYC, the other in London. They need a very simple program to
# find out if the branches are open or closed. The hours of BOTH branches
# are 9am to 5pm in their own time zone
#
# Challenge Objective: Utilize datetime function to determine curent times in
# Portland, NYC, and London. Then compare branch hours to see if they're opened
# or closed.


# import datetime modues and any others to aid in time zone calculations
from datetime import datetime
import time
import pytz
utc= pytz.utc


# create script to determine curent times in Portland, NYC, and London.
Portland = pytz.timezone('US/Pacific')
NYC = pytz.timezone('US/Eastern')
London = pytz.timezone('Europe/London')

P_curr = datetime.now(Portland)
N_curr = datetime.now(NYC)
L_curr = datetime.now(London)

#Then compare branch hours to see if they're opened or closed.
Branch_Open = time.strftime("%H"[9])

Branch_Close =time.strftime("%H"[17])



#print out the three branches and whether or not they're open.

print("Welcome to our Portland Branch! The current time is ", P_curr.strftime('%H:%M'))

if P_curr >= Branch_Open and time_curr <= time_close:
    print("This Branch is currently open")
else:
    print("We apologize, but this branch is currently closed. We will be glad to serve you during business hours.")


print("Welcome to our NYC Branch! The current time is ", N_curr.strftime('%H:%M'))

if N_curr >= time_open and time_curr <= time_close:
    print("This Branch is currently open")
else:
    print("We apologize, but this branch is currently closed. We will be glad to serve you during business hours.")



print("Welcome to our London Branch! The current time is ", L_curr.strftime('%H:%M'))
if L_curr >= time_open and time_curr <= time_close:
    print("This Branch is currently open")
else:
    print("We apologize, but this branch is currently closed. We will be glad to serve you during business hours.")








