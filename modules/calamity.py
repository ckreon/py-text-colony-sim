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
		gv['weather'] = rng(1,3)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(1,3)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(9,12)
		log_task('birthrate')
		
	elif (gv['rng'] <= 4):
		# Second Branch
		log_task('branch', 'second')
		# Roll Weather
		gv['weather'] = rng(3,5)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(5,7)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(15,20)
		log_task('birthrate')

	elif (gv['rng'] <= 6):
		# Third Branch		
		log_task('branch', 'third')
		# Roll Weather
		gv['weather'] = rng(5,7) 
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(6,8)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(6,9)
		log_task('birthrate')

	elif (gv['rng'] <= 8):
		# Fourth Branch		
		log_task('branch', 'fourth')
		# Roll Weather
		gv['weather'] = rng(6,8)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(3,5)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(12,15)
		log_task('birthrate')

	elif (gv['rng'] == 9):
		# Fifth Branch
		log_task('branch', 'fifth')
		# Roll Weather
		gv['weather'] = rng(7,10)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,10)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(1,6)
		log_task('birthrate')

	elif (gv['rng'] == 10):
		# Sixth Branch
		log_task('branch', 'sixth')
		# Roll Weather
		gv['weather'] = rng(7,10)
		log_task('weather')
		# Roll Immunity
		gv['immunity'] = rng(7,10)
		log_task('immunity')
		# Roll Birthrate
		gv['birthrate'] = rng(1,6)
		log_task('birthrate')

	ltxt('Calamity has set Weather to: ' + weather[gv['weather']])
	ltxt('Calamity has set Immunity to: ' + immunity[gv['immunity']])
	ltxt('Calamity has set Birthrate to: ' + str(gv['birthrate']))

def log_task(task, branch=''):
	if (task == 'branch'):
		ltxt('Entered ' + branch + ' branch of calamity tree')
	elif (task == 'weather'):
		ltxt('Weather variable set to: ' + str(gv['weather']))
	elif (task == 'immunity'):
		ltxt('Immunity variable set to: ' + str(gv['immunity']))
	elif (task == 'birthrate'):
		ltxt('Birthrate variable set to: ' + str(gv['birthrate']))