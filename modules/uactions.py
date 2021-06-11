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
def manage_farmers():
	getting_input = True

	while (getting_input):
		utxt('How many Farmers would you like to modify?')
		new_farmers = user_number()
		
		if (new_farmers > 0):
			if (gv['free_pop'] >= new_farmers):
				gv['farmers'] += new_farmers
				gv['free_pop'] -= new_farmers
				getting_input = False
			else:
				utxt('You don\'t have enough Free Population for that.')
		elif (new_farmers < 0):
			if (gv['farmers'] >= new_farmers):
				gv['farmers'] += new_farmers
				gv['free_pop'] += new_farmers
				getting_input = False
			else:
				utxt('You don\'t have enough Farmers for that.')

	utxt('You have ' + str(gv['farmers']) + ' Farmers.')

# run farm function
def farm():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Farm Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] <= 5):
		# normal outcome
		utxt('It was a normal month on the Farms.')
		calamity = 0

	elif (gv['rng'] <= 7):
		# poor outcome
		utxt('It was a bad month on the Farms.')
		calamity = -2

	elif (gv['rng'] <= 9):
		# great outcome
		utxt('It was a great month on the Farms!')
		calamity = 3

	elif (gv['rng'] == 10):
		# awful outcome
		utxt('It was a terrible month on the Farms!')
		calamity = -3

	ltxt('Farm Calamity is now set to: ' + str(calamity))

	food = ((gv['farmers']*3) + calamity)
	utxt('You generated ' + str(food) + ' food this turn.')

	gv['food'] = (gv['food'] + food)
	utxt('You now have ' + str(gv['food']) + ' food in storage.')
