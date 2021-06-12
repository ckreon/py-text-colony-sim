#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run metals function with calamity
def metals():
	calamity = 0
	ltxt('RNG Seed is set to: ' + str(gv['rng']))
	ltxt('Metals Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] >= 9):
		# normal outcome
		print_status('normal')
		calamity = 0

	elif (gv['rng'] >= 6):
		# good outcome
		print_status('good')
		calamity = 2

	elif (gv['rng'] >= 3):
		# bad outcome
		print_status('bad')
		calamity = -2

	elif (gv['rng'] == 2):
		# great outcome
		print_status('great')
		calamity = 3

	elif (gv['rng'] == 1):
		# terrible outcome
		print_status('terrible')
		calamity = -3

	ltxt('Metals Calamity is now set to: ' + str(calamity))

	# Generate iron
	iron = ((gv['miners']*2) + calamity)
	utxt('You generated ' + str(iron) + ' iron this turn.', 0.3, False)
	# Add generated iron to storage
	gv['iron'] = (gv['iron'] + iron)
	utxt('You now have ' + str(gv['iron']) + ' iron in storage.', 0.3, False)
	# Generate gold
	gold = ((gv['miners']) + calamity)
	utxt('You generated ' + str(gold) + ' gold this turn.', 0.3, False)
	# Add generated gold to storage
	gv['gold'] = (gv['gold'] + gold)
	utxt('You now have ' + str(gv['gold']) + ' gold in storage.')

def print_status(status):
	utxt(('It was a ' + status + ' month at the Mines:'), 0.3, False)