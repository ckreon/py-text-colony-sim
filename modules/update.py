#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import game_over


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
def update():
	print('-- (2) Updating!' + newline)

	print('-- Eating food...' + newline)
	# set 'food' value equal to current food minus current population
	gv['food'] = gv['food'] - gv['population']

	if (gv['food'] < 0):
		print('-- Your colony has run out of food and starved.')
		print('-- Good try, though.')
		game_over()

	print('-- Using health supplies...' + newline)
	# set 'health' value equal to currenth health minus current population
	gv['health'] = gv['health'] - gv['population']

	if (gv['health'] < 0):
		print('-- Your colony has run out of health and died.')
		print('-- Solid effort, though.')
		game_over()