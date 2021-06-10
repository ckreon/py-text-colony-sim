#// IMPORTS //#
import os	# os utilities library


#// GLOBAL VARIABLES //#
gv = {
	'app_run':		True,
	'running':		False,
	'main_menu':	True,
	'new_game':		False,
	'world_size':	10,
	'day':			1,
	'month':		1,
	'year':			1,
	'rng':			0,
	'population':	10,
	'free_pop':		10,
	'farmers':		0,
	'doctors':		0,
	'lumbers':		0,
	'miners':		0,
	'food':			100,
	'wood':			100,
	'iron':			100,
	'gold':			100,
	'health':		100,
	'newline':		os.linesep
}

world_grid = {}