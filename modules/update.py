#// IMPORTS //#
from modules.config		import gv
from modules.helpers	import ltxt
from modules.helpers	import rng
from modules.helpers	import date_update
from modules.calamity	import calamity
from modules.farm		import farm
from modules.health		import health
from modules.lumber		import lumber
from modules.metals		import metals
from modules.population	import population


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

	# update population
	ltxt('Calling population function')
	population()

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