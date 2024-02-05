import classes as cl
import pygame
import script

# Initializing Important Stuff
clock = pygame.time.Clock()
game = cl.game()

screenChangeParameter = -1
mouseInTerminal = False
updateScreen = True
screenHeight = 0
screenWidth = 0
count = 0
fps = 60


# Initializing Script
script = script.script(game)
scriptLength = len(script.script)

# Game Loop
while game.running:

	if count < scriptLength:
		script.advance(game)
		updateScreen = True

	screen = {"width": game.screen.get_size()[0], "height": game.screen.get_size()[1]}

	if screen["width"] != screenWidth:
		screenChangeParameter = 0
		updateScreen = True

	if screen["height"] != screenHeight:
		screenChangeParameter = 1
		updateScreen = True

	if updateScreen:

		game.terminalLine = 0

		# Girl Test
		script.update()
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

	count += 1
	clock.tick(fps)
