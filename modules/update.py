#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import rng
from modules.helpers	import date_update
from modules.calamity	import calamity
from modules.uactions	import farm
from modules.uactions	import health
from modules.uactions	import lumber
from modules.uactions	import metals


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#
def update():
	ltxt('Updating!')
	
	# set the RNG seed for this loop
	ltxt('Prior to randomization, RNG is set to: ' + str(gv['rng']))
	gv['rng'] = rng()
	ltxt('After randomization, RNG is set to: ' + str(gv['rng']))

	# build the base Calamity tree based off the RNG seed
	ltxt('Calling calamity function')
	calamity()

	# update date
	ltxt('Calling date_update function')
	date_update()

	# farm
	ltxt('Calling farm function')
	farm()

	# health
	ltxt('Calling health function')
	health()

	# lumber
	ltxt('Calling health function')
	lumber()

	# metals
	ltxt('Calling metals function')
	metals()