
############################################################
#
#                      TEXT COLONY SIM                      
#
############################################################
#  Hand-Coded Organic Artisanal Fair-Trade Ingredients by:  
############################################################
#               /                                           
#      ___     / ___      __      ___      ___       __     
#    //   ) ) //\ \     //  ) ) //___) ) //   ) ) //   ) )  
#   //       //  \ \   //      //       //   / / //   / /   
#  ((____   //    \ \ //      ((____   ((___/ / //   / /    
#                                                           
############################################################
#               Corey Kozlowski (c) 2020/2021               
############################################################

#// IMPORTS //#
import sys
from modules.config		import gv
from modules.menus		import main_menu
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.process	import process_events
from modules.update		import update
from modules.draw		import draw


#// ARGS //#
if (len(sys.argv) > 1):
	if (sys.argv[1] == "--verbose"):
		gv['verbose'] = True


#// VARIABLES //#
newline = gv['newline']


#// INITIALIZE //#
print(newline + newline + newline)
print('================================================')
print('=============                      =============')
print('========                                ========')
print('=====                                      =====')
print('===                                          ===')
print('=          Welcome to TEXT COLONY SIM          =')
print('=                 Please clap.                 =')
print('===                                          ===')
print('=====                                      =====')
print('========                                ========')
print('=============                      =============')
print('================================================')
print(newline + newline + newline)
utxt('')


#// MAIN APP LOOP //#
# while 'app_run' is true, run the app loop
while gv['app_run']:
	# if the 'main_menu' variable is 'True', run it
	if (gv['main_menu']):
		main_menu()

	#// MAIN GAME LOOP //#
	# while 'running' is true, run the game loop
	while gv['running']:
		# use our custom 'ltxt' function to print log text
		ltxt('Starting Main Loop!')
		# execute the main loop functions
		draw()				# render main text on screen
		update()			# update all objects that need updating
		process_events()	# process inputs and other stuff, including quit
		# print more log text
		ltxt('Main Loop finished!')