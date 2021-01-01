#// IMPORTS //#
from config		import gv
from helpers	import press_enter
from helpers	import user_quit


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
def process_events():
	print('-- (1) Processing events!')
	print('-- \'running\' is set to: ' + str(gv['running']) + newline)
	# force user to hit key to continue
	press_enter()
	# check if user wants to quit
	user_quit()