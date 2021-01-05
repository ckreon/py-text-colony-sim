
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
from modules.config		import gv
from modules.menu		import main_menu
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.process	import process_events
from modules.update		import update
from modules.draw		import draw


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


#// MAIN APP LOOP //#
# while 'app_run' is true, run the app loop
while gv['app_run']:
	# if the 'main_menu' variable is 'True', run it
	if (gv['main_menu']):
		main_menu()

	#// MAIN GAME LOOP //#
	# while 'running' is true, run the game loop
	while gv['running']:
		ltxt('Starting Main Loop!')
		process_events()	# process inputs and other stuff, including quit
		update()			# update all objects that need updating
		draw()				# render things on screen
		ltxt('Main Loop finished!')