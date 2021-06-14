#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import press_enter
from modules.helpers	import game_over


#// FUNCTIONS //#
def process_events():
	ltxt('Processing events!')
	food_used = gv['population']
	health_used = gv['population']
	wood_used = round(gv['population'] * 0.5)
	iron_used = round(gv['population'] * 0.4)
	gold_used = round(gv['population'] * 0.3)

	ltxt('Starting stats update')

	# update food
	utxt('Using ' + str(food_used) + ' food...', 0.3, False)
	# set 'food' value equal to current food minus current population
	gv['food'] -= food_used

	# update health
	utxt('Using ' + str(health_used) + ' health...', 0.3, False)
	# set 'health' value equal to current health minus current population
	gv['health'] -= health_used

	# update wood
	utxt('Using ' + str(wood_used) + ' wood...', 0.3, False)
	# set 'wood' value equal to current wood minus current population
	gv['wood'] -= wood_used

	# update metals
	utxt('Using ' + str(iron_used) + ' iron...', 0.3, False)
	utxt('Using ' + str(gold_used) + ' gold...')
	# set 'iron' and 'gold' values equal to current values minus
	# current population
	gv['iron'] -= iron_used
	gv['gold'] -= gold_used
	
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