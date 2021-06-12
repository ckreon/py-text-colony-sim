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

	if (gv['rng'] >= 6):
		# normal outcome
		utxt('It was a normal month at the Mines:', 0.3, False)
		calamity = 0

	elif (gv['rng'] >= 4):
		# poor outcome
		utxt('It was a bad month at the Mines:', 0.3, False)
		calamity = -2

	elif (gv['rng'] >= 2):
		# great outcome
		utxt('It was a great month at the Mines:', 0.3, False)
		calamity = 3

	elif (gv['rng'] == 1):
		# awful outcome
		utxt('It was a terrible month at the Mines:', 0.3, False)
		calamity = -3

	ltxt('Metals Calamity is now set to: ' + str(calamity))

	iron = ((gv['miners']*2) + calamity)
	utxt('You generated ' + str(iron) + ' iron this turn.', 0.3, False)

	gv['iron'] = (gv['iron'] + iron)
	utxt('You now have ' + str(gv['iron']) + ' iron in storage.', 0.3, False)
	
	gold = ((gv['miners']) + calamity)
	utxt('You generated ' + str(gold) + ' gold this turn.', 0.3, False)

	gv['gold'] = (gv['gold'] + gold)
	utxt('You now have ' + str(gv['gold']) + ' gold in storage.')
