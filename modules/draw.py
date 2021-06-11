#// IMPORTS //#
from modules.config		import gv
from modules.menus		import game_menu
from modules.helpers	import ltxt
from modules.helpers	import utxt


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
# main draw function
def draw():
	ltxt('Drawing!')
	game_menu()