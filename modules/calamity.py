from modules.config		import gv
from modules.config		import weather
from modules.config		import immunity
from modules.helpers	import ltxt
from modules.helpers	import rng

def calamity():
	ltxt('Starting calamity tree...')
	ltxt('RNG Seed is set to: ' + str(gv['rng']))

	# Define the base RNG tree
	if (gv['rng'] <= 2):
		# First Branch
		log_task('branch', 'first')
		# Roll Weather
		gv['weather'] = rng(1,2)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(1,2)
		log_task('immunity')
		
	elif (gv['rng'] <= 4):
		# Second Branch
		log_task('branch', 'second')
		# Roll Weather
		gv['weather'] = rng(3,4)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(6,9)
		log_task('immunity')

	elif (gv['rng'] <= 6):
		# Third Branch		
		log_task('branch', 'third')
		# Roll Weather
		gv['weather'] = rng(5,6) 
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(5,10)
		log_task('immunity')

	elif (gv['rng'] <= 8):
		# Fourth Branch		
		log_task('branch', 'fourth')
		# Roll Weather
		gv['weather'] = rng(7,8)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(3,4)
		log_task('immunity')

	elif (gv['rng'] == 9):
		# Fifth Branch
		log_task('branch', 'fifth')
		# Roll Weather
		gv['weather'] = rng(7,9)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,8)
		log_task('immunity')

	elif (gv['rng'] == 10):
		# Sixth Branch
		log_task('branch', 'sixth')
		# Roll Weather
		gv['weather'] = rng(8,10)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,8)
		log_task('immunity')

	ltxt('Calamity has set Weather to: ' + weather[gv['weather']])
	ltxt('Calamity has set Immunity to: ' + immunity[gv['immunity']])

def log_task(task, branch=''):
	if (task == 'branch'):
		ltxt('Entered ' + branch + ' branch of calamity tree')
	if (task == 'immunity'):
		ltxt('Immunity variable set to: ' + str(gv['immunity']))
	elif (task == 'weather'):
		ltxt('Weather variable set to: ' + str(gv['weather']))