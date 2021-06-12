#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run health function with calamity
def health():
	calamity = 0
	ltxt('Immunity Seed is set to: ' + str(gv['immunity']))
	ltxt('Health Calamity is currently set to: ' + str(calamity))

	if (gv['immunity'] <= 2):
		# good outcome
		print_status('good')
		calamity = 2

	elif (gv['immunity'] <= 4):
		# normal outcome
		print_status('normal')
		calamity = 0

	elif (gv['immunity'] <= 6):
		# great outcome
		print_status('great')
		calamity = 4

	elif (gv['immunity'] <= 8):
		# bad outcome
		print_status('bad')
		calamity = -2

	elif (gv['immunity'] <= 10):
		# terrible outcome
		print_status('terrible')
		calamity = -4

	ltxt('Health Calamity is now set to: ' + str(calamity))

	# Generate health
	health = ((gv['doctors']*3) + calamity)
	utxt('You generated ' + str(health) +
	     ' health supplies this turn.', 0.3, False)
	# Add generated health to storage
	gv['health'] = (gv['health'] + health)
	utxt('You now have ' + str(gv['health']) +
	     ' health supplies in storage.')

def print_status(status):
	utxt(('It was a ' + status + ' month at the Hospitals:'), 0.3, False)