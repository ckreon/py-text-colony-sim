#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import press_enter


#// FUNCTIONS //#
def process_events():
	ltxt('Processing events!')
	#print('-- \'running\' is set to: ' + str(gv['running']) + newline)
	
	pop = (
			gv['free_pop'] + gv['farmers'] + gv['doctors'] +
			gv['lumbers'] + gv['miners']
		)
	gv['population'] = pop

	# run the press_enter function, forcing user to hit key to continue
	press_enter()
