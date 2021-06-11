#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import press_enter


#// FUNCTIONS //#
def process_events():
	ltxt('Processing events!')
	
	# process population for this loop
	pop = (
			gv['free_pop'] + gv['farmers'] + gv['doctors'] +
			gv['lumbers'] + gv['miners']
		)
	gv['population'] = pop

	# run the press_enter function, forcing user to hit key to continue
	press_enter()
