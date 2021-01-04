#// IMPORTS //#
import re	# regular expression library
from modules.config import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# this method should ask the user if they'd like to quit
# if they answer yes, it should actually quit, if not, wheel
def user_quit():
	# get user input (with a prompt), and store it in 'quit_input'
	quit_input = input('>> Do you want to quit? ')
	print()
	# use a regular expression to check 'quit' for 'y/yes' (any case)
	if (re.match(r'^(y|ya|yes|)$', quit_input, re.IGNORECASE)):
		# if yes, change running to 'False' and quit
		gv['running'] = False
		print('-- \'running\' is set to: ' + str(gv['running']) + newline)
		#quit()	# commented out to prove loop stops when 'running' is False
	else:
		# otherwise keep running ('else' isn't needed, just here for posterity)
		print('-- Still looping!')
		print('-- \'running\' is set to: ' + str(gv['running']) + newline)

# this method should ask the user to press enter to continue
# nothing should happen until they press enter
def press_enter():
	print('Press ENTER to continue...')

	# the following works because the 'input' function won't conclude
	# without a CR (carriage return), which the 'Enter' key provides

	# force user to hit ENTER to continue
	input()