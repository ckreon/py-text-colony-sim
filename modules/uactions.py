#// IMPORTS //#
from modules.helpers	import ltxt
from modules.helpers	import utxt
from modules.helpers	import user_number
from modules.config		import gv


#// VARIABLES //#
newline = gv['newline']


#// FUNCTIONS //#

# add citizens to the farm profession
def manage_workers(worker_type):
	getting_input = True

	ltxt('Starting input loop for worker management')
	while (getting_input):
		utxt('How many ' + worker_type + ' would you like to modify?')
		new_workers = user_number()
		ltxt('User Input returned as: ' + str(new_workers))

		if (new_workers > 0):
			ltxt('User Input is greater than 0')
			if (gv['free_pop'] >= new_workers):
				gv[worker_type] += new_workers
				gv['free_pop'] -= new_workers
				getting_input = False
			else:
				utxt('You don\'t have enough Free Population for that.')
		elif (new_workers < 0):
			ltxt('User Input is less than 0')
			if (gv[worker_type] >= abs(new_workers)):
				gv[worker_type] -= abs(new_workers)
				gv['free_pop'] += abs(new_workers)
				getting_input = False
			else:
				utxt('You don\'t have enough ' + worker_type + ' for that.')
		elif (new_workers == 0):
			ltxt('User Input is 0')
			getting_input = False

	utxt('You have ' + str(gv[worker_type]) + ' ' + worker_type + '.')

# run farm function with calamity
def farm():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Farm Calamity is currently set to: ' + str(calamity))

	if (gv['weather'] <= 4):
		# normal outcome
		utxt('The weather provided a normal month on the Farms.')
		calamity = 0

	elif (gv['weather'] <= 6):
		# poor outcome
		utxt('The weather provided a great month on the Farms.')
		calamity = 4

	elif (gv['weather'] <= 8):
		# great outcome
		utxt('The weather provided a bad month on the Farms!')
		calamity = -2

	elif (gv['weather'] <= 10):
		# awful outcome
		utxt('The weather provided a terrible month on the Farms!')
		calamity = -4

	ltxt('Farm Calamity is now set to: ' + str(calamity))

	food = ((gv['farmers']*3) + calamity)
	utxt('You generated ' + str(food) + ' food this turn.')

	gv['food'] = (gv['food'] + food)
	utxt('You now have ' + str(gv['food']) + ' food in storage.')

# run health function with calamity
def health():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Health Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] >= 6):
		# normal outcome
		utxt('It was a normal month at the Hospitals.')
		calamity = 0

	elif (gv['rng'] >= 4):
		# poor outcome
		utxt('It was a bad month at the Hospitals.')
		calamity = -2

	elif (gv['rng'] >= 2):
		# great outcome
		utxt('It was a great month at the Hospitals!')
		calamity = 3

	elif (gv['rng'] == 1):
		# awful outcome
		utxt('It was a terrible month at the Hospitals!')
		calamity = -3

	ltxt('Health Calamity is now set to: ' + str(calamity))

	health = ((gv['doctors']*3) + calamity)
	utxt('You generated ' + str(health) + ' health supplies this turn.')

	gv['health'] = (gv['health'] + health)
	utxt('You now have ' + str(gv['health']) + ' health supplies in storage.')

# run lumber function with calamity
def lumber():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Lumber Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] <= 5):
		# normal outcome
		utxt('It was a normal month at the Lumbermills.')
		calamity = 0

	elif (gv['rng'] <= 7):
		# poor outcome
		utxt('It was a bad month at the Lumbermills.')
		calamity = -2

	elif (gv['rng'] <= 9):
		# great outcome
		utxt('It was a great month at the Lumbermills!')
		calamity = 3

	elif (gv['rng'] == 10):
		# awful outcome
		utxt('It was a terrible month at the Lumbermills!')
		calamity = -3

	ltxt('Lumber Calamity is now set to: ' + str(calamity))

	wood = ((gv['lumbers']*4) + calamity)
	utxt('You generated ' + str(wood) + ' wood this turn.')

	gv['wood'] = (gv['wood'] + wood)
	utxt('You now have ' + str(gv['wood']) + ' wood in storage.')

# run metals function with calamity
def metals():
	calamity = 0
	ltxt('RNG is set to: ' + str(gv['rng']))
	ltxt('Metals Calamity is currently set to: ' + str(calamity))

	if (gv['rng'] >= 6):
		# normal outcome
		utxt('It was a normal month at the Mines.')
		calamity = 0

	elif (gv['rng'] >= 4):
		# poor outcome
		utxt('It was a bad month at the Mines.')
		calamity = -2

	elif (gv['rng'] >= 2):
		# great outcome
		utxt('It was a great month at the Mines!')
		calamity = 3

	elif (gv['rng'] == 1):
		# awful outcome
		utxt('It was a terrible month at the Mines!')
		calamity = -3

	ltxt('Metals Calamity is now set to: ' + str(calamity))

	iron = ((gv['miners']*2) + calamity)
	utxt('You generated ' + str(iron) + ' iron this turn.')

	gv['iron'] = (gv['iron'] + iron)
	utxt('You now have ' + str(gv['iron']) + ' iron in storage.')
	
	gold = ((gv['miners']) + calamity)
	utxt('You generated ' + str(gold) + ' gold this turn.')

	gv['gold'] = (gv['gold'] + gold)
	utxt('You now have ' + str(gv['gold']) + ' gold in storage.')