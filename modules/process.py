#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import overview
from modules.helpers	import press_enter
from modules.helpers	import user_quit


#// FUNCTIONS //#
def process_events():
	ltxt('Processing events!')
	#print('-- \'running\' is set to: ' + str(gv['running']) + newline)

	# the following functions are imports, check their respective files
	overview()
	# run the press_enter function, forcing user to hit key to continue
	press_enter()
	# run the user_quit function, check if user wants to quit
	#user_quit()