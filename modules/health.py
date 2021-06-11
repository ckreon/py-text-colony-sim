#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run health function with calamity
def health():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Health Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] >= 6):
		# normal outcome
		utxt('It was a normal month at the Hospitals:', 0.3, False)
		calamity = 0

	elif (gv['rng'] >= 4):
		# poor outcome
		utxt('It was a bad month at the Hospitals:', 0.3, False)
		calamity = -2

	elif (gv['rng'] >= 2):
		# great outcome
		utxt('It was a great month at the Hospitals:', 0.3, False)
		calamity = 3

	elif (gv['rng'] == 1):
		# awful outcome
		utxt('It was a terrible month at the Hospitals:', 0.3, False)
		calamity = -3

	ltxt('Health Calamity is now set to: ' + str(calamity))

	health = ((gv['doctors']*3) + calamity)
	utxt('You generated ' + str(health) +
	     ' health supplies this turn.', 0.3, False)

	gv['health'] = (gv['health'] + health)
	utxt('You now have ' + str(gv['health']) +
	     ' health supplies in storage.')
