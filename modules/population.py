#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.config		import gv


#// FUNCTIONS //#

def population():
	ltxt('Birthrate variable is set to: ' + str(gv['birthrate']))

	# Calculate birthrate percentage (0.1 - 2)
	birthrate = gv['birthrate'] / 10
	ltxt('Birthrate percentage set to: ' + str(birthrate))

	# Calculate new population to add and round to a whole number
	new_pop = round(
	          (gv['free_pop'] * birthrate * (gv['population'] / 2.5)) / 10
	          )
	utxt('You generated ' + str(new_pop) + ' people this round.', 0.3, False)
	
	# Add new population to free population
	gv['free_pop'] += new_pop

	# Process total population for this loop
	total_pop = (
			gv['free_pop'] + gv['farmers'] + gv['doctors'] +
			gv['lumbers'] + gv['miners']
			)
	gv['population'] = total_pop
	utxt('You now have ' + str(gv['population']) + ' people in total.')