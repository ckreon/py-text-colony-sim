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

	if (gv['rng'] <= 5):
		# normal outcome
		utxt('It was a normal month at the Lumbermills:', 0.3, False)
		calamity = 0

	elif (gv['rng'] <= 7):
		# poor outcome
		utxt('It was a bad month at the Lumbermills:', 0.3, False)
		calamity = -2

	elif (gv['rng'] <= 9):
		# great outcome
		utxt('It was a great month at the Lumbermills:', 0.3, False)
		calamity = 3

	elif (gv['rng'] == 10):
		# awful outcome
		utxt('It was a terrible month at the Lumbermills:', 0.3, False)
		calamity = -3

	ltxt('Lumber Calamity is now set to: ' + str(calamity))

	wood = ((gv['lumbers']*4) + calamity)
	utxt('You generated ' + str(wood) + ' wood this turn.', 0.3, False)

	gv['wood'] = (gv['wood'] + wood)
	utxt('You now have ' + str(gv['wood']) + ' wood in storage.')
