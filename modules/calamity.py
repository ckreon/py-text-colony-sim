from modules.config		import gv
from modules.config		import weather
from modules.config		import immunity
from modules.helpers	import ltxt
from modules.helpers	import rng

def calamity():
	ltxt('Starting Calamity tree...')
	ltxt('RNG Seed is set to: ' + str(gv['rng']))
	# Define the base RNG tree
	if (gv['rng'] <= 2):
		ltxt('Entered first branch of calamity tree.')
		# First Branch
		# Roll Weather
		gv['weather'] = rng(1,2)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(1,2)
		log_task('immunity')
		
	elif (gv['rng'] <= 4):
		ltxt('Entered second branch of calamity tree.')
		# Second Branch
		# Roll Weather
		gv['weather'] = rng(3,4)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(6,9)
		log_task('immunity')

	elif (gv['rng'] <= 6):
		ltxt('Entered third branch of calamity tree.')
		# Third Branch
		gv['weather'] = rng(5,6) 
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(5,10)
		log_task('immunity')

	elif (gv['rng'] <= 8):
		ltxt('Entered fourth branch of calamity tree.')
		# Fourth Branch
		gv['weather'] = rng(7,8)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(3,4)
		log_task('immunity')

	elif (gv['rng'] == 9):
		ltxt('Entered fifth branch of calamity tree.')
		# Fifth Branch
		gv['weather'] = rng(7,9)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,8)
		log_task('immunity')

	elif (gv['rng'] == 10):
		ltxt('Entered sixth branch of calamity tree.')
		# Sixth Branch
		gv['weather'] = rng(8,10)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,8)
		log_task('immunity')

	ltxt('Calamity has set Weather to: ' + weather[gv['weather']])
	ltxt('Calamity has set Immunity to: ' + immunity[gv['immunity']])

def log_task(task):
	if (task == 'immunity'):
		ltxt('Immunity variable set to: ' + str(gv['immunity']))
	elif (task == 'weather'):
		ltxt('Weather variable set to: ' + str(gv['weather']))