#// IMPORTS //#
import re	# regular expression library
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt


#// FUNCTIONS //#
def main_menu():
	# set the 'main_menu' variable to 'False' so we don't loop
	gv['main_menu'] = False
	getting_input = True

	while getting_input:
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
		utxt('Would you like to:', 0.2, False)
		utxt('| 1 | Manage Workers', 0, False)
		utxt('| Q | Quit Game', 0, False)
		u_input = input('>> ')
		print()

		if (u_input == '1'):
			utxt('Managing workforce!', 0.5)
			getting_input = False
			worker_menu()
		elif (re.match(r'^(q|quit)$', u_input, re.IGNORECASE)):
			utxt('Quitting...')
			getting_input = False
			quit()
		else:
			utxt('I\'m not sure what that is.')

def worker_menu():
	utxt('Worker Menu - Under Construction')