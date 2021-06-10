from modules.config		import gv
from modules.config		import weather
from modules.helpers	import ltxt
from modules.helpers	import rng

def calamity():
	# Define the base RNG tree
	if (gv['rng'] <= 2):
		# First Branch
		gv['weather'] = rng(1,2)

	elif (gv['rng'] <= 4):
		# Second Branch
		gv['weather'] = rng(3,4)

	elif (gv['rng'] <= 6):
		# Third Branch
		gv['weather'] = rng(5,6) 

	elif (gv['rng'] <= 8):
		# Fourth Branch
		gv['weather'] = rng(7,8)

	elif (gv['rng'] == 9):
		# Fifth Branch
		gv['weather'] = 9

	elif (gv['rng'] == 10):
		# Sixth Branch
		gv['weather'] = 10

	ltxt('Calamity has set Weather to: ' + weather[gv['weather']])