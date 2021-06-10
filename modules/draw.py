#// IMPORTS //#
from modules.config		import gv
from modules.menus		import game_menu
from modules.helpers	import ltxt
from modules.helpers	import utxt


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# this function should provide the user with an overview
# of the current game-state (stats, terrain, warnings, etc.)
def overview():
	# concatenate the date variables into a string called 'game_date'
	game_date = (
		str(gv['month']) + '-' + str(gv['day']) + '-' + str(gv['year'])
	)
	# print the various stats
	utxt(('Date: ' + game_date), 0, False)
	utxt(('Total Population: ' + str(gv['population'])), 0, False)
	utxt(('Free Population: ' + str(gv['free_pop'])), 0, False)
	utxt(('Farmers: ' + str(gv['farmers'])), 0, False)
	utxt(('Doctors: ' + str(gv['doctors'])), 0, False)
	utxt(('Lumbers: ' + str(gv['lumbers'])), 0, False)
	utxt(('Miners: ' + str(gv['miners'])), 0, False)
	utxt(('Food: ' + str(gv['food'])), 0, False)
	utxt(('Wood: ' + str(gv['wood'])), 0, False)
	utxt(('Iron: ' + str(gv['iron'])), 0, False)
	utxt(('Gold: ' + str(gv['gold'])), 0, False)
	utxt(('Health: ' + str(gv['health'])), 0.7)

def draw():
	ltxt('Drawing!')
	overview()
	game_menu()