#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

# run farm function with calamity
def farm():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Farm Calamity is currently set to: ' + str(calamity))

	if (gv['weather'] <= 4):
		# normal outcome
		utxt('The weather made for a normal month on the Farms:', 0.3, False)
		calamity = 0

	elif (gv['weather'] <= 6):
		# poor outcome
		utxt('The weather made for a great month on the Farms:', 0.3, False)
		calamity = 4

	elif (gv['weather'] <= 8):
		# great outcome
		utxt('The weather made for a bad month on the Farms:', 0.3, False)
		calamity = -2

	elif (gv['weather'] <= 10):
		# awful outcome
		utxt('The weather made for a terrible month on the Farms:', 0.3, False)
		calamity = -4

	ltxt('Farm Calamity is now set to: ' + str(calamity))

	food = ((gv['farmers']*3) + calamity)
	utxt('You generated ' + str(food) + ' food this turn.', 0.3, False)

	gv['food'] = (gv['food'] + food)
	utxt('You now have ' + str(gv['food']) + ' food in storage.')
