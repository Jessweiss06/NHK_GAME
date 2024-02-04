import classes as cl
import pygame
import script

import byoeimero
import rei

# Initializing Important Stuff
clock = pygame.time.Clock()
game = cl.game()

screenChangeParameter = -1
mouseInTerminal = False
updateScreen = True
screenHeight = 0
screenWidth = 0
fps = 60


# Initializing Script
byoeimero = byoeimero.init(game)
rei = rei.init(game)

girls = [byoeimero, rei]

script.init(game, girls)

script.advance(game)
script.advance(game)

# Game Loop
while game.running:

	screen = {"width": game.screen.get_size()[0], "height": game.screen.get_size()[1]}

	if screen["width"] != screenWidth:
		screenChangeParameter = 0
		updateScreen = True

	if screen["height"] != screenHeight:
		screenChangeParameter = 1
		updateScreen = True

	if updateScreen:

		byoeimero.pointer = 0
		game.terminalLine = 0

		# Girl Test
		rei.drawFrame()
		game.terminalDraw()
		game.loadTerminalCache()
		screenHeight = game.screen.get_size()[1]
		screenWidth = game.screen.get_size()[0]
		updateScreen = False

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game.running = False
			pygame.quit()

	clock.tick(fps)
