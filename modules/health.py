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
		utxt('It was a good month at the Hospitals:', 0.3, False)
		calamity = 2

	elif (gv['immunity'] <= 4):
		# normal outcome
		utxt('It was a normal month at the Hospitals:', 0.3, False)
		calamity = 0

	elif (gv['immunity'] <= 6):
		# great outcome
		utxt('It was a great month at the Hospitals:', 0.3, False)
		calamity = 4

	elif (gv['immunity'] <= 8):
		# poor outcome
		utxt('It was a bad month at the Hospitals:', 0.3, False)
		calamity = -2

	elif (gv['immunity'] <= 10):
		# awful outcome
		utxt('It was a terrible month at the Hospitals:', 0.3, False)
		calamity = -4

	ltxt('Health Calamity is now set to: ' + str(calamity))

	health = ((gv['doctors']*3) + calamity)
	utxt('You generated ' + str(health) +
	     ' health supplies this turn.', 0.3, False)

	gv['health'] = (gv['health'] + health)
	utxt('You now have ' + str(gv['health']) +
	     ' health supplies in storage.')
