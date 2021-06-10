#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import rng
from modules.helpers	import game_over
from modules.calamity	import calamity


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
def update():

	ltxt('Updating!')
	
	# set the RNG seed for this loop
	ltxt('Prior to randomization, RNG is set to: ' + str(gv['rng']))
	gv['rng'] = rng()
	ltxt('After randomization, RNG is set to: ' + str(gv['rng']))

	# build the base Calamity tree based off the RNG seed
	calamity()

	utxt('Eating food...', 0.7)
	# set 'food' value equal to current food minus current population
	gv['food'] = gv['food'] - gv['population']

	if (gv['food'] < 0):
		utxt('Your colony has run out of food and starved.', 0.7, False)
		utxt('Good try, though.')
		game_over()

	utxt('Using health supplies...', 0.7)
	# set 'health' value equal to currenth health minus current population
	gv['health'] = gv['health'] - gv['population']

	if (gv['health'] < 0):
		utxt('Your colony has run out of health and died.', 0.7, False)
		utxt('Solid effort, though.')
		game_over()