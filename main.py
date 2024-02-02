import classes as cl
import pygame

clock = pygame.time.Clock()
game = cl.game()
fps = 60

print("\n\n\nRunning...")

# Girl init
byoeimero = cl.girl(game)
byoeimero.imageLocation = "Byoeimero_Yuokini\\NHK_Concept.png"
byoeimero.imageResolution = (413, 584)
byoeimero.name = "Byoeimero"
byoeimero.dialogueArray = [
("Hello Tatsuhiro UWU", 0)
]


while game.running:

	# Girl Test
	byoeimero.draw(byoeimero.dialogueArray[byoeimero.pointer][0])

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			game.running = False
			pygame.quit()

	clock.tick(fps)
