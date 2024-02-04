import classes as cl
import byoeimero
import rei

def init(game, girls):

	global pointer
	global script

	global byoeimero
	global rei

	byoeimero = girls[0]
	rei = girls[1]

	game.terminalCache = []

	pointer = 0
	script = [
	(byoeimero, cl.game.format2),
	(rei, cl.game.format3)
	]

def advance(game):

	global pointer
	global script

	if pointer != len(script):
		script[pointer][0].advance(script[pointer][1])
		pointer += 1
