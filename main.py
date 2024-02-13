import classes as cl
import pygame
import script


# <Initializing Important Stuff>
clock = pygame.time.Clock()
game = cl.game()

terminal = cl.terminal(game)
# </Initializing Important Stuff>


# <Declaring Important Variables>
screenChangeParameter = -1
updateScreen = True
screenHeight = 0
screenWidth = 0
command = ""
fps = 30
# </Declaring Important Variables>


# <Initializing Script>
script = script.script(game, terminal)
scriptLength = len(script.script)
# </Initializing Script>


# <Game Loop>
while game.running:

	if script.pointer < scriptLength and not script.halt:
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

		terminal.line = 0

		# <Redrawing Frame>
		script.currentGirl.drawFrame(script.currentGirl.currentFrame)
		terminal.draw()
		terminal.loadCache()
		# </Redrawing Frame>

		screenHeight = game.screen.get_size()[1]
		screenWidth = game.screen.get_size()[0]
		updateScreen = False

		pygame.display.flip()

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game.running = False
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				script.pointer += 1
				script.halt = False
				script.run(command)
				command = ""

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE: 
				command = command[:-1] 
			else: 
				command += event.unicode


	clock.tick(fps)
# </Game Loop>
