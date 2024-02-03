import pygame

class game:

	pointer = 0
	terminalLine = 0
	terminalWidth = 400
	terminalMargine = 10
	terminalLineHeight = 14

	# In dialogue Arrays:
	# 0 means the dialogue is finished
	# 1 means the dialogue continues to the next index

	dialogueArray = [
	("Please Enter A Name", 0)
	]

	def __init__(self):

		pygame.font.init()
		icon = pygame.image.load('icon.png')
		pygame.display.set_caption("Galge")
		pygame.display.set_icon(icon)

		self.screen = pygame.display.set_mode((900, 675), pygame.RESIZABLE)
		pygame.display.flip()

		self.running = True

	def terminalDraw(self):

		screenSize = self.screen.get_size()
		game.terminalMargine = 10

		xPosition = (screenSize[0] - game.terminalWidth)
		yPosition = game.terminalMargine
		width = game.terminalWidth - game.terminalMargine
		length = screenSize[1] - game.terminalMargine * 2

		terminal = pygame.Rect(xPosition, yPosition, width, length)

		color = (0, 0, 0)
		pygame.draw.rect(self.screen, color, terminal)
		pygame.display.flip()

	def terminalWrite(self, text, font, size, color):

		my_font = pygame.font.SysFont(font, size)
		text_surface = my_font.render(text, True, color)
		innerMargine = 3
		xOrigin = (self.screen.get_size()[0] - game.terminalWidth) + innerMargine
		yOrigin = game.terminalMargine + innerMargine + game.terminalLine * game.terminalLineHeight
		terminalOrigin = (xOrigin, yOrigin)

		self.screen.blit(text_surface, (terminalOrigin))
		pygame.display.flip()

		game.terminalLine += 1

	def clearScreen(self):
		self.screen.fill((250, 245, 240))

class protagonist:

	def __init__(self, name):
		self.name = name
		self.reputation = 0

class girl:

	# "girl" needs an instance of the class "game"
	# because "screen" is an attribute of the instance
	# not the class

	def __init__(self, game):

		self.game = game
		self.pointer = 0
		self.affection = 0

		self.name = ""
		self.dialogueArray = []

		self.imageScaler = 1
		self.imageLocation = ""
		self.imageResolution = []

	def setPointer(self, position):
		self.pointer = position

	def setAffection(self, amount):
		self.affection = amount

	def advance(self):
		return f"{self.dialogueArray[self.pointer][0]}"

	def apraise(self):
		name = self.name
		affection = self.affection
		finalS = "s" if affection != 1 else ""
		return f"{name} has {affection} affection point{finalS}"

	def drawFrame(self):

		self.game.clearScreen()

		scaledImage = (self.imageResolution[0] * self.imageScaler, self.imageResolution[1] * self.imageScaler)
		self.image = pygame.image.load(self.imageLocation)
		self.image = pygame.transform.scale(self.image, scaledImage)
		screenWidth = self.game.screen.get_size()[0]
		imageWidth = scaledImage[0]
		imageOrigin = (screenWidth - imageWidth) / 2
		imageCenterCoordinate = (screenWidth - (imageWidth + game.terminalWidth)) / 2


		self.game.screen.blit(self.image, (imageCenterCoordinate, 0))
		pygame.display.flip()
