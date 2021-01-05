#// IMPORTS //#
import re	# regular expression library
from modules.config	import gv
from modules.menu	import main_menu



#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# this function should set the 'running' variable to 'False'
# and end the current game, returning user to the main menu
def game_over():
	gv['running'] = False
	main_menu()
	
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
		print('-- \'running\' is set to: ' + str(gv['running']) + newline)
		#quit()	# commented out to prove loop stops when 'running' is False
	else:
		# otherwise keep running ('else' isn't needed, just here for posterity)
		print('-- Still looping!')
		print('-- \'running\' is set to: ' + str(gv['running']) + newline)

# this function should ask the user to press enter to continue
# nothing should happen until they press enter
def press_enter():
	print('-- Press ENTER to continue...')

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
	print('-- Date: ' + game_date)
	print('-- Population: ' + str(gv['population']))
	print('-- Food: ' + str(gv['food']))
	print('-- Wood: ' + str(gv['wood']))
	print('-- Iron: ' + str(gv['iron']))
	print('-- Gold: ' + str(gv['gold']))
	print('-- Health: ' + str(gv['health']) + newline)

	print('-- At some point, this will ask you for some input' + newline)