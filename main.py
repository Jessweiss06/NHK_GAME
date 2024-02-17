import classes as cl
import pygame
import script


# <Initializing Important Stuff>
clock = pygame.time.Clock()
game = cl.game()

terminal = cl.terminal(game)
script = script.script(game, terminal)
userIO = cl.userIO(script)
# </Initializing Important Stuff>


# <Declaring Important Variables>
scriptLength = len(script.script)
fps = 30
# </Declaring Important Variables>



# <Game Loop>
while game.running:

	currentScreenWidth = game.screen.get_size()[0]
	currentScreenHeight = game.screen.get_size()[1]

	# advancing game and scheduling screen update if possible
	if script.pointer < scriptLength and not script.halt:
		game.screenUpdateScheduled = True
		script.advance(game)

	# scheduling screen update if the window was resized
	screenWidthChanged = currentScreenWidth != game.screenWidth
	screenHeightChanged = currentScreenHeight != game.screenHeight
	screenChanged = screenWidthChanged or screenHeightChanged
	#game.screenUpdateScheduled = screenChanged or game.screenUpdateScheduled
	if screenChanged: game.screenUpdateScheduled = True

	# updating screen if needed
	if game.screenUpdateScheduled: game.updateScreen(terminal, script)

	cl.event.handle(cl.event.raised)
	userIO.handle()
	clock.tick(fps)
# </Game Loop>
