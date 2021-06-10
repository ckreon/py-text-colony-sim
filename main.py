
############################################################
#
#                      TEXT COLONY SIM                      
#
############################################################
#  Hand-Coded Organic Artisanal Fair-Trade Ingredients by:  
############################################################
#   ________.__                  ___.          .__        
#  /  _____/|  |__   ____ ___.__.\_ |__   ____ |__|_______
# /   \  ___|  |  \_/ __ <   |  | | __ \ /  _ \|  \___   /
# \    \_\  \   Y  \  ___/\___  | | \_\ (  <_> )  |/    / 
#  \______  /___|  /\___  > ____| |___  /\____/|__/_____ \
#         \/     \/     \/\/          \/                \/
############################################################
#        Corey Kozlowski & Andy Riches (c) 2020/2021        
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
utxt('', 1)


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