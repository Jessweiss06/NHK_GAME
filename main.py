import classes as cl
import pygame

clock = pygame.time.Clock()
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

	if game.screen.get_size()[0] != screenWidth:
		# Girl Test
		green = (0, 150, 0)
		byoeimero.drawFrame()
		game.terminalDraw()
		game.terminalWrite(byoeimero.dialogueArray[byoeimero.pointer][0], "Monokai", 20, green)
		byoeimero.pointer += 1
		game.terminalWrite(byoeimero.dialogueArray[byoeimero.pointer][0], "Monokai", 20, green)
		screenWidth = game.screen.get_size()[0]

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game.running = False
			pygame.quit()

	clock.tick(fps)
