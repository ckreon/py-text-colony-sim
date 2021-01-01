#// IMPORTS //#
import re		# regular expression library
from config import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
def main_menu():
	getting_input = True

	while getting_input:
		print('Would you like to:')
		print('| 1 | Start a New Game')
		print('| Q | Quit Game')
		u_input = input('>> ')
		print()

		if (u_input == '1'):
			print('Let the adventures begin!' + newline)
			getting_input = False
			gv['running'] = True
		elif (re.match(r'^(q|quit)$', u_input, re.IGNORECASE)):
			print('Quitting...' + newline)
			getting_input = False
			quit()
		else:
			print('I\'m not sure what that is.' + newline)