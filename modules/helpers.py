#// IMPORTS //#
import re	# regular expression library
import time	# time functions library
from modules.config		import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# this function should print a string to the console,
# sleep for a set amount of seconds, and add a newline
def ltxt(l_string):
	# print string and add newline (defined in config to be OS correct)
	print('** (Log) ' + l_string + newline)
	# sleep for the provided amount of seconds
	time.sleep(0.5)

# this function should print a string to the console and sleep for a provided
# amount of seconds after printing the text, adding a newline by default
def utxt(u_string, u_sleep=1, u_newline=True):
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

# this function should provide the user with an overview
# of the current game-state (stats, terrain, warnings, etc.)
def overview():
	# concatenate the date variables into a string called 'game_date'
	game_date = (
		str(gv['month']) + '-' + str(gv['day']) + '-' + str(gv['year'])
	)
	# print the various stats
	utxt(('Date: ' + game_date), 0, False)
	utxt(('Population: ' + str(gv['population'])), 0, False)
	utxt(('Food: ' + str(gv['food'])), 0, False)
	utxt(('Wood: ' + str(gv['wood'])), 0, False)
	utxt(('Iron: ' + str(gv['iron'])), 0, False)
	utxt(('Gold: ' + str(gv['gold'])), 0, False)
	utxt(('Health: ' + str(gv['health'])), 0.7)

	utxt('At some point, this will ask you for some input')