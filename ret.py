# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:24:55 2021
"""


from datetime import date #import library for date

Retire_age=65#Assign retirement age 
print("Hello Sir/Ma'am!")#just print Hello Sir/Ma'am!
name_p = input ("Enter your name :")#user prompt to get name of the employee
age_p = int(input ("Enter your age :"))#user prompt to get age of the employee
today = date.today()#Fetching today date
	
d2 = int(today.strftime(" %Y"))#Fetching current year
if age_p > 65:#print message for age should not more than 65 years
    print('Sorry {0}! You are not eligible to work here!.You are already retired!'.format(name_p))
elif age_p == 65:#print message if age is equal to 65 year
    print('Hi {1}! You are going to retire very shortly at {0}'.format(d2,name_p))
else:#print message if age is less than 65 year----

    Remaining_years=Retire_age-age_p
    Ret_year=d2+Remaining_years
    print('Congratulations {0}! You have to work for {1} more years and your retirerment will be at {2}'.format(name_p,Remaining_years,Ret_year))