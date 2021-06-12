#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run farm function with calamity
def farm():
	calamity = 0
	ltxt('Weather Seed is set to: ' + str(gv['weather']))
	ltxt('Farm Calamity is currently set to: ' + str(calamity))

	if (gv['weather'] <= 2):
		# good outcome
		print_status('good')
		calamity = 2

	elif (gv['weather'] <= 4):
		# normal outcome
		print_status('normal')
		calamity = 0

	elif (gv['weather'] <= 6):
		# great outcome
		print_status('great')
		calamity = 4

	elif (gv['weather'] <= 8):
		# bad outcome
		print_status('bad')
		calamity = -2

	elif (gv['weather'] <= 10):
		# terrible outcome
		print_status('terrible')
		calamity = -4

	ltxt('Farm Calamity is now set to: ' + str(calamity))

	# Generate food
	food = ((gv['farmers']*3) + calamity)
	utxt('You generated ' + str(food) + ' food this turn.', 0.3, False)
	# Add generated food to storage
	gv['food'] = (gv['food'] + food)
	utxt('You now have ' + str(gv['food']) + ' food in storage.')

def print_status(status):
	utxt(('It was a ' + status + ' month on the Farms:'), 0.3, False)