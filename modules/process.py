#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import press_enter


#// FUNCTIONS //#
def process_events():
	ltxt('Processing events!')
	
	# process population for this loop
	pop = (
			gv['free_pop'] + gv['farmers'] + gv['doctors'] +
			gv['lumbers'] + gv['miners']
		)
	gv['population'] = pop

	ltxt('Starting stats update')
	# update food
	utxt('Eating food...')
	# set 'food' value equal to current food minus current population
	gv['food'] -= gv['population']

	# update health
	utxt('Using health supplies...')
	# set 'health' value equal to current health minus current population
	gv['health'] -= gv['population']

	# update wood
	utxt('Using wood...')
	# set 'wood' value equal to current wood minus current population
	gv['wood'] -= (round(gv['population'] * 0.5))

	# update metals
	utxt('Using metals...')
	# set 'iron' and 'gold' values equal to current values minus
	# current population
	gv['iron'] -= (round(gv['population'] * 0.5))
	gv['gold'] -= (round(gv['population'] * 0.2))

	if (gv['food'] < 0):
		utxt('Your colony has run out of food and starved.', 0.5, False)
		utxt('Good try, though.')
		game_over()
	elif (gv['health'] < 0):
		utxt('Your colony has run out of health and died.', 0.5, False)
		utxt('Solid effort, though.')
		game_over()
	elif (gv['wood'] < 0):
		utxt('Your colony has run out of wood and died.', 0.5, False)
		utxt('Nice run, though.')
		game_over()
	elif (gv['iron'] < 0):
		utxt('Your colony has run out of iron and died.', 0.5, False)
		utxt('Decent round, though.')
		game_over()
	elif (gv['gold'] < 0):
		utxt('Your colony has run out of gold and died.', 0.5, False)
		utxt('Great attempt, though.')
		game_over()

	# run the press_enter function, forcing user to hit key to continue
	press_enter()