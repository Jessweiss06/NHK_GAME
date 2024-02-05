import pygame

class game:

	pointer = 0
	terminalLine = 0
	terminalWidth = 400
	terminalMargine = 10
	terminalLineHeight = 14
	terminalCache = [("text", "format")]

	red = (150, 0, 0)
	gray = (5, 10, 20)
	green = (0, 150, 0)
	salmon = (235, 80, 72)
	pink = (255, 208, 207)

	format1 = ("Mister Sirloin", 20, red)
	format2 = ("Monokai", 20, salmon)
	format3 = ("Monokai", 20, green)

	# In dialogue Arrays:
	# 0 means the dialogue is finished
	# 1 means the dialogue continues from the previous index

	dialogueArray = [
	("Please Enter A Name", 0)
	]

	def __init__(self):

		self.terminalHeight = 0
		pygame.font.init()
		icon = pygame.image.load('icon.png')
		pygame.display.set_caption("Gal Game")
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

		self.terminalHeight = length

		terminal = pygame.Rect(xPosition, yPosition, width, length)

		pygame.draw.rect(self.screen, game.pink, terminal)
		pygame.display.flip()

	def terminalWrite(self, text, textFormat):

		linesInTerminal = int(self.terminalHeight / self.terminalLineHeight)
		if self.terminalLine == linesInTerminal:
			self.terminalCache = []

		print(linesInTerminal)
		font, size, color = textFormat
		my_font = pygame.font.SysFont(font, size)
		text_surface = my_font.render(text, True, color)
		innerMargine = 3
		xOrigin = (self.screen.get_size()[0] - game.terminalWidth) + innerMargine
		yOrigin = game.terminalMargine + innerMargine + self.terminalLine * game.terminalLineHeight
		terminalOrigin = (xOrigin, yOrigin)

		self.screen.blit(text_surface, (terminalOrigin))
		pygame.display.flip()

		self.terminalLine += 1

	def loadTerminalCache(self):

		for entry in self.terminalCache:
			self.terminalWrite(entry[0], entry[1])

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
		self.dialogueArray = ["dialogue", "end or continue"]

		self.imageScaler = 1
		self.imageLocation = ""
		self.imageResolution = []

	def setPointer(self, position):
		self.pointer = position

	def setAffection(self, amount):
		self.affection = amount

	def advance(self, frmt):

		self.game.terminalCache.append((self.dialogueArray[self.pointer][0], frmt))
		self.pointer += 1

		while self.dialogueArray[self.pointer][1] == 1:
			self.game.terminalCache.append((self.dialogueArray[self.pointer][0], frmt))
			self.pointer += 1

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
