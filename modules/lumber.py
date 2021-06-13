#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run lumber function with calamity
def lumber():
	calamity = 0
	ltxt('RNG Seed is set to: ' + str(gv['rng']))
	ltxt('Lumber Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] <= 2):
		# normal outcome
		print_status('normal')
		calamity = 0

	elif (gv['rng'] <= 5):
		# good outcome
		print_status('good')
		calamity = 2

	elif (gv['rng'] <= 8):
		# bad outcome
		print_status('bad')
		calamity = -2

	elif (gv['rng'] == 9):
		# great outcome
		print_status('great')
		calamity = 3

	elif (gv['rng'] == 10):
		# terrible outcome
		print_status('terrible')
		calamity = -3

	ltxt('Lumber Calamity is now set to: ' + str(calamity))

	wood = ((gv['lumbers'] * 4) + calamity)
	utxt('You generated ' + str(wood) + ' wood this turn.', 0.3, False)

	gv['wood'] = (gv['wood'] + wood)
	utxt('You now have ' + str(gv['wood']) + ' wood in storage.')

def print_status(status):
	utxt(('It was a ' + status + ' month at the Lumbermills:'), 0.3, False)