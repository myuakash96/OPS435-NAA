#!/usr/bin/env python3
"""
OPS435 Assignment 1 - Winter 2021
Program: a1_myuakash.py (replace student_id with your Seneca User name)
Author: "myuakash"
The python code in this file is original work written by
Md Yasin Uddin Akash. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading (except git).  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import os
import sys
global argstep
argstep = ""

# Usage function is defined to refer to later
def usage():
	"""
	Prints the usage of the script in a helpful manner
	"""
	use = """
	Usage: a1_myuakash.py [--step] YYYYMMDD +/-n
    Takes a valid date (DATE) and a number of days (NUMDAYS)
    and returns a certain number of days specified...
    Positional Arguments:
    --step - Verbosely prints each day to the result
    DATE - Date in YYYYMMDD format
    NUMDAYS - Number of days forward or backward (backward is denoted by a -)
    e.g. a1_myuakash.py 20190101 4
         a1_myuakash.py --step 20180204 1
         a1_myuakash.py --step 20180101 -2 
    """
	print (use)
	exit()

def valid_date(argdate):
	"""
	valid_date(date) -> str
		valid_date() takes a date string in 'YYYYMMDD' format and returns a 
		True or false statement relaying if it is a valid date.
		e.g. valid_date('20171231') -> 'True'
			 valid_date('20188132') -> 'False'
			 valid_date('Alphabet') -> 'False'
	"""
	#Testing of the date entered is actually a date
	if isinstance(argdate, int):
		argdate = str(argdate)
	if len(argdate) != 8 or not argdate.isdigit():
		print("Error: wrong date entered")
		return("False")

	#Split the entered value into YYYY/MM/DD
	argyear = argdate[0:4]
	#print ("Year = " + str(argyear))

	argmonth = argdate[4:6]
	#print ("Month = " + str(argmonth))

	argday = argdate[6:8]
	#print ("Day = " + str(argday))

	#Check to see if valid month or day is entered
	if int(argmonth) > 12:
		print("Error: wrong month entered")
		return("False")
	elif int(argday) > 31:
		print ("Error: wrong day entered")
		return("False")
	else:
		return("True")


def leap_year(argyear):
	"""
	leap_year(argyear) -> str
		leap_year() takes a valid year string in 'YYYY' format and returns a 
		True/False statement corelating to if its a a leap year.'
		e.g. leap_year('2018') -> 'False'
			 leap_year('1600') -> 'True'
			 leap_year('2152') -> 'True'
	"""
#Checking the script if year is a leap year
	lyear = argyear % 4
	if lyear == 0:
		lyearstatus = "True" # This is a leap year
	else:
		lyearstatus = "False"
	lyear = argyear % 100
	if lyear == 0:
		lyearstatus = "False"
	lyear = argyear % 400
	if lyear == 0:
		lyearstatus = "True"
	return(lyearstatus)

def days_in_mon(year):
	if isinstance(year, str):
		year = int(year)
	#Check to see if leap_year exists, if exists, add days to feburary
	if leap_year(year) == "True":
		feb_max = 29
	else:
		feb_max = 28

	#MaxMonth is the maximum number of days per month (#:# = Month:Day)
	MaxMonth = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return(MaxMonth)

def tomorrow(argdate):
	"""
	tomorrow(argdate) -> str
		tomorrow() takes a valid date string in 'YYYYMMDD' format and returns 
		a date string for the next day in 'YYYYMMDD' format.
		e.g. tomorrow('20171231') -> '20180101'
	     	 tomorrow('20180131') -> '20180201'
	    	 tomorrow('20180228') -> '20180301'
	"""
	#Function will return tomorrow's date with argument argdate given
	if isinstance(argdate, int):
		argdate = str(argdate)
	if valid_date(argdate) == "True":
		argyear = int(argdate[0:4])
		argmonth = int(argdate[4:6])
		argday = int(argdate[6:])
		#Resultant will be what day we want to return, which is the next day
		resultday = argday + 1

		#MaxMonth is the maximum number of days per month, (#:# = Month:Day)
		MaxMonth = days_in_mon(argyear)

		#If the day is above the maximum number of days for the month, cycle to the next month as the first day

		if resultday > MaxMonth[argmonth]:
			varday = resultday % MaxMonth[argmonth]
			resultmonth = argmonth + 1
		else:
			varday = resultday
			resultmonth = argmonth
		if resultmonth > 12:
			varmonth = 1
			varyear  = argyear + 1
		else:
			varmonth = resultmonth
			varyear = argyear
		nextdate = str(varyear)+str(varmonth).zfill(2)+str(varday).zfill(2)
		return nextdate
	else:
		exit()


def yesterday(argdate):
	"""yesterday(argdate) -> str
	yesterday() takes a valid year string in 'YYYYMMDD' format and returns a
	date string for the previous day in 'YYYYMMDD' format.
	e.g. yesterday('20171231') -> '20171230'
	yesterday('20180131') -> '20180130'
	yesterday('20180228') -> '20180227'
	
	"""
	#Function returns yesterday's date with argument argdate given
	if isinstance(argdate, int):
		argdate = str(argdate)
	if valid_date(argdate) == "True":
		argyear = int(argdate[0:4])
		argmonth = int(argdate[4:6])
		argday = int(argdate[6:])
		#Check to see if leap_year exists, if exists, add days to feburary
		if leap_year(argyear) == "True":
			feb_max = 29
		else:
			feb_max = 28

		#Resultant will be what day we want to return, which is the next day
		resultday = argday - 1

		#MaxMonth is the maximum number of days per month, (#:# = Month:Day)
		MaxMonth = days_in_mon(argyear)

		#If the day is above the max number of days for the month, cycle to next month but in reverse

		if resultday < 1:
		#Change the day
			resultmonth = argmonth - 1
			if resultmonth < 1:
					varday = 31
			else:
				changement = MaxMonth[resultmonth]
				varday = changement
		else:
			varday = resultday
			resultmonth = argmonth
		if resultmonth < 1:
		#Change the month
			varmonth = 12
			varyear  = argyear - 1
		else:
			varmonth = resultmonth
			varyear = argyear
		nextdate = str(varyear)+str(varmonth).zfill(2)+str(varday).zfill(2)
		return nextdate
	else:
		exit()


def dbda(argdate,days):
	"""
	dbda(argdate,days) -> str
		dbda() takes a valid date string in 'YYYYMMDD' format, along with the number
		of days forward or backward and returns the date string before or after that date
		in 'YYYYMMDD' format.
		e.g. dbda('20171231','1') -> '20180101'
			 dbda('20180131','-1') -> '20180130'
			 dbda('20180228','4') -> '20180304'
	"""
		#Rounding Days such that it always returns a whole number
	global argstep
	if __name__ != "__main__":
		argstep = "False"
	days = round(int(days))
	#If the days are positive, run the tomorrow function
	if days > 0:
		if argstep == "True":
			print(tomorrow(argdate))
		tomorrowdate = tomorrow(argdate)
		while days != 1:
			tomorrowdate = tomorrow(tomorrowdate)
			if argstep == "True":
				print(str(tomorrowdate))
			days = days - 1
		if argstep == "False":
			print(str(tomorrowdate))

	#If the days are negative, yesterday function is ran
	elif days < 0:
		if argstep == "True":
			print (yesterday(argdate))
		yesterdaydate = yesterday(argdate)
		while days != -1:
			yesterdaydate = yesterday(yesterdaydate)
			if argstep == "True":
				print(str(yesterdaydate))
			days = days + 1
		if argstep == "False":
			print(str(yesterdaydate))
	else:
			days = 0
			return argdate

if __name__ == "__main__":
	if ((len(sys.argv) >= 5 or len(sys.argv) <= 2)):
		usage()
	if sys.argv[1] == "--step":
		argstep = "True"
		argdate = sys.argv[2]
		argoption = sys.argv[3]
		dbda(argdate,argoption)
	else:
		argstep = "False"
		argdate = sys.argv[1]
		argoption = sys.argv[2]
		dbda(argdate,argoption)
#end of the code
