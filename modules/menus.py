#// IMPORTS //#
import re	# regular expression library
from modules.config		import gv
from modules.config		import weather
from modules.helpers	import ltxt
from modules.helpers	import utxt


#// FUNCTIONS //#
def main_menu():
	# set the 'main_menu' variable to 'False' so we don't loop
	gv['main_menu'] = False
	getting_input = True

	while getting_input:
		utxt('--MAIN MENU--', 0.2, False)
		utxt('Would you like to:', 0.2, False)
		utxt('| 1 | Start a New Game', 0, False)
		utxt('| Q | Quit Game', 0, False)
		u_input = input('>> ')
		print()

		if (u_input == '1'):
			utxt('Let the simulation begin!')
			getting_input	= False
			gv['running']	= True
			gv['new_game']	= True
		elif (re.match(r'^(q|quit)$', u_input, re.IGNORECASE)):
			utxt('Quitting...')
			getting_input = False
			quit()
		else:
			utxt('I\'m not sure what that is.')

def game_menu():
	getting_input = True

	while getting_input:
		# draw the overview
		overview()
		# draw the menu
		utxt('--GAME MENU--', 0.2, False)
		utxt('Would you like to:', 0.2, False)
		utxt('| 1 | Manage Farmers', 0, False)
		utxt('| 2 | Manage Doctors', 0, False)
		utxt('| 3 | Manage Lumbers', 0, False)
		utxt('| 4 | Manage Miners', 0, False)
		utxt('| 5 | Process Turn', 0, False)
		utxt('| Q | Quit Game', 0, False)
		u_input = input('>> ')
		print()

		if (u_input == '1'):
			utxt('Managing Farmers!')
			# get input/manage farmers

		elif (u_input == '2'):
			utxt('Managing Doctors!')
			# get input/manage doctors

		elif (u_input == '3'):
			utxt('Managing Lumbers!')
			# get input/manage lumbers

		elif (u_input == '4'):
			utxt('Managing Miners!')
			# get input/manage miners

		elif (u_input == '5'):
			utxt('Processing Turn!')
			getting_input = False
			# get input/manage miners

		elif (re.match(r'^(q|quit)$', u_input, re.IGNORECASE)):
			utxt('Quitting...')
			getting_input = False
			quit()
		else:
			utxt('I\'m not sure what that is.')

# this function should provide the user with an overview
# of the current game-state (stats, terrain, warnings, etc.)
def overview():
	# concatenate the date variables into a string called 'game_date'
	game_date = (
		str(gv['month']) + '-' + str(gv['day']) + '-' + str(gv['year'])
	)
	# print the various stats
	utxt('--OVERVIEW--', 0, False)	
	utxt(('Date: ' + game_date), 0, False)
	utxt(('Weather: ' + weather[gv['weather']]), 0, False)
	utxt(('Total Population: ' + str(gv['population'])), 0, False)
	utxt(('Free Population: ' + str(gv['free_pop'])), 0, False)
	utxt(('Farmers: ' + str(gv['farmers'])), 0, False)
	utxt(('Doctors: ' + str(gv['doctors'])), 0, False)
	utxt(('Lumbers: ' + str(gv['lumbers'])), 0, False)
	utxt(('Miners: ' + str(gv['miners'])), 0, False)
	utxt(('Food: ' + str(gv['food'])), 0, False)
	utxt(('Wood: ' + str(gv['wood'])), 0, False)
	utxt(('Iron: ' + str(gv['iron'])), 0, False)
	utxt(('Gold: ' + str(gv['gold'])), 0, False)
	utxt(('Health: ' + str(gv['health'])), 0.2)
