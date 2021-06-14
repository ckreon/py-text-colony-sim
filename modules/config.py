#// IMPORTS //#
import os	# os utilities library


#// GLOBAL VARIABLES //#
gv = {
	'app_run':		True,
	'running':		False,
	'verbose':		False,
	'main_menu':	True,
	'day':			1,
	'month':		1,
	'year':			1,
	'rng':			0,
	'weather':		1,
	'immunity':		1,
	'birthrate':	10,
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

weather = {
	1:	'Normal',
	2:	'Overcast',
	3:	'Windy',
	4:	'Cool',
	5:	'Warm',
	6:	'Hot',
	7:	'Rainy',
	8:	'Thunderstorm',
	9:	'Heat Snap',
	10:	'Cold Snap'
}

immunity = {
	1:	'Normal',
	2:	'Above Average',
	3:	'Below Average',
	4:	'Weakened',
	5:	'Strong',
	6:	'Boosted',
	7:	'Cold Virus',
	8:	'Flu Virus',
	9:	'Plague',
	10:	'Pandemic'
}