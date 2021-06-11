#// IMPORTS //#
import re		# regular expression library
import time		# time functions library
import random	# random functions library
from modules.config		import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# this function should generate a random number between 1 and 10
def rng(lower_limit=1, upper_limit=10):
	# picks a random number between the upper and lower limit
	return random.randint(lower_limit, upper_limit)

# this function should print a string to the console,
# sleep for a set amount of seconds, and add a newline
def ltxt(l_string):
	# if debug mode is enabled, print the log text, otherwise skip
	if (gv['verbose']):
		# print string and add newline (defined in config to be OS correct)
		print('** (Log) ' + l_string + newline)
		# sleep for the provided amount of seconds
		time.sleep(0.5)

# this function should print a string to the console and sleep for a provided
# amount of seconds after printing the text, adding a newline by default
def utxt(u_string, u_sleep=0.5, u_newline=True):
	# if 'u_newline' is 'True'
	if (u_newline):
		# print string and add newline (defined in config to be OS correct)
		print('-- ' + u_string + newline)
	else:
		# print string
		print('-- ' + u_string)
	# sleep for the provided amount of seconds
	time.sleep(u_sleep)

# this function should set the 'running' variable to 'False'
# and end the current game, returning user to the main menu
def game_over():
	# set 'running' variable to 'False' to end the game after this loop
	gv['running']	= False
	# set 'main_menu' variable to 'True' so we get a menu next loop
	gv['main_menu']	= True
	
# this function should get user input about a yes or no question
# if they answer yes, it should return true, if no, return false
def yes_or_no():
	# get user input (with a prompt), and store it in 'user_input'
	user_input = input('>> ')
	print()
	# use a regular expression to check input for 'y/yes' (any case)
	if (re.match(r'^(y|ya|yes|)$', user_input, re.IGNORECASE)):
		# if yes, return true
		return True
	else:
		# otherwise return false
		return False

# this function should get user input and return it
def user_input():
	# return user input (with a prompt)
	return input('>> ')

# this function should get a number from the user, validate it, and return it
def user_number():
	getting_input = True

	while (getting_input):
		number = input('>> ')

		if (int(number)):
			getting_input = False
		else:
			utxt('Must be a number!')

	return number

# this function should update the date by one day, including
# adjusting the month and year as necessary per gregorian calendar
def date_update():
	# make local variables for easier use
	day		= gv['day']
	month	= gv['month']
	year	= gv['year']
	# variables to store days of current month
	months_in_year	= 12
	days_in_month	= 31

	# set days_in_month to be correct for current month
	if (month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
		days_in_month = 31
	elif (month == 4 or 6 or 9 or 11):
		days_in_month = 30
	elif (month == 2):
		days_in_month = 28

	# advance date by one day if not the last day of the month
	if (day < days_in_month):
		day += 1
	# if it is the last day of the month, set the day back to 1
	elif (day == days_in_month):
		day = 1
		# advance the date by one month if not the last month of the year
		if (month < months_in_year):
			month += 1
		# if it is the last month of the year, set the month back to 1
		elif (month == months_in_year):
			month = 1
			# advance date by one year
			year += 1

	gv['day']	= day
	gv['month']	= month
	gv['year']	= year

# this function should ask the user if they'd like to quit
# if they answer yes, it should actually quit, if not, wheel
def user_quit():
	# get user input (with a prompt), and store it in 'quit_input'
	quit_input = input('>> Do you want to quit? ')
	print()
	# use a regular expression to check 'quit' for 'y/yes' (any case)
	if (re.match(r'^(y|ya|yes|)$', quit_input, re.IGNORECASE)):
		# if yes, change running to 'False' and quit
		gv['running'] = False
		ltxt('\'running\' is set to: ' + str(gv['running']))
		#quit()	# commented out to prove loop stops when 'running' is False
	else:
		# otherwise keep running ('else' isn't needed, just here for posterity)
		utxt('Still looping!', 0 , False)
		ltxt('\'running\' is set to: ' + str(gv['running']))

# this function should ask the user to press enter to continue
# nothing should happen until they press enter
def press_enter():
	utxt('Press ENTER to continue...', 0)

	# the following works because the 'input' function won't conclude
	# without a CR (carriage return), which the 'Enter' key provides

	# force user to hit ENTER to continue
	input()
