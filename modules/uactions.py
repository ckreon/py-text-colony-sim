#// IMPORTS //#
import re		# regular expression library
import time		# time functions library
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import yes_or_no
from modules.helpers	import user_number
from modules.config		import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# add citizens to the farm profession
def add_farmers():
	utxt('Would you like to assign new farmers?')
	if (yes_or_no()):
		utxt('How many farmers would you like to assign?')
		new_farmers = user_number()

		if (gv['free_pop'] >= new_farmers):
			gv['farmers'] = (gv['farmers'] + new_farmers)
			gv['free_pop'] = (gv['free_pop'] - new_farmers)
		else:
			utxt('You don\'t have enough population for that.')

	utxt('You have ' + str(gv['farmers']) + ' farmers.')

def farm():
	# ask user if they want to add farmers
	add_farmers()

	# run farm function
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] <= 5):
		# normal outcome
		utxt('It was a normal day on the farms.')
		calamity = 0

	elif (gv['rng'] <= 7):
		# poor outcome
		utxt('It was a bad day on the farms.')
		calamity = -2

	elif (gv['rng'] <= 9):
		# great outcome
		utxt('It was a great day on the farms!')
		calamity = 3

	elif (gv['rng'] == 10):
		# awful outcome
		utxt('It was a terrible day on the farms!')
		calamity = -3

	ltxt('Calamity is now set to: ' + str(calamity))

	food = ((gv['farmers']*3) + calamity)
	utxt('You generated ' + str(food) + ' food this turn.')
	
	gv['food'] = (gv['food'] + food)
	utxt('You now have ' + str(gv['food']) + ' food in storage.')
