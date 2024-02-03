import classes as cl
import pygame

clock = pygame.time.Clock()
screenChangeParameter = -1
mouseInTerminal = False
updateScreen = True
screenHeight = 0
game = cl.game()
screenWidth = 0
fps = 60

print("\n\n\nRunning...")

# Girl init
byoeimero = cl.girl(game)
byoeimero.imageLocation = "Byoeimero_Yuokini\\NHK_Concept.png"
byoeimero.imageResolution = (1690, 3508)
byoeimero.imageScaler = 1/6
byoeimero.name = "Byoeimero"
byoeimero.dialogueArray = [
("Hello Tatsuhiro", 0),
("I'm Byoeimero UWU", 0)
]

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
		byoeimero.drawFrame()
		game.terminalDraw()
		game.terminalWrite(byoeimero.dialogueArray[0][0], cl.game.format2)
		game.terminalWrite(byoeimero.dialogueArray[1][0], cl.game.format2)
		screenHeight = game.screen.get_size()[1]
		screenWidth = game.screen.get_size()[0]
		updateScreen = False

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game.running = False
			pygame.quit()

	clock.tick(fps)
