
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

main_menu()

#// MAIN APP LOOP //#
while gv['app_run']:

	#// MAIN GAME LOOP //#
	while gv['running']:
		print('-- Starting Main Loop!' + newline)
		process_events()	# process inputs and other stuff, including quit
		update()			# update all objects that need updating
		draw()				# render things on screen
		print('-- Main Loop finished!' + newline)