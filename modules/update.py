#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import rng
from modules.helpers	import date_update
from modules.helpers	import game_over
from modules.calamity	import calamity
from modules.uactions	import farm
from modules.uactions	import health


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
	ltxt('Calling calamity function')
	calamity()

	# update date
	ltxt('Calling date_update function')
	date_update()

	# farm
	ltxt('Calling farm function')
	farm()

	# health
	ltxt('Calling health function')
	health()
	
	# update stats
	update_stats()


def update_stats():
	# update food
	utxt('Eating food...')
	# set 'food' value equal to current food minus current population
	gv['food'] = gv['food'] - gv['population']

	# update health
	utxt('Using health supplies...')
	# set 'health' value equal to currenth health minus current population
	gv['health'] = gv['health'] - gv['population']

	if (gv['food'] < 0):
		utxt('Your colony has run out of food and starved.', 0.5, False)
		utxt('Good try, though.')
		game_over()
	elif (gv['health'] < 0):
		utxt('Your colony has run out of health and died.', 0.5, False)
		utxt('Solid effort, though.')
		game_over()
