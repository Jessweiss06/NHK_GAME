import pygame

class game:

	pointer = 0

	red = (150, 0, 0)
	gray = (5, 10, 20)
	green = (0, 150, 0)
	blue = (137, 169, 201)
	salmon = (235, 80, 72)
	pink = (255, 208, 207)

	format1 = ("Mister Sirloin", 20, red)
	format2 = ("Monokai", 20, salmon)
	format3 = ("Monokai", 20, green)
	format4 = ("Monokai", 20, blue)
	format5 = ("Monokai", 20, gray)

	command = ""

	# In dialogue Arrays:
	# 0 means the dialogue is finished
	# 1 means the dialogue continues from the previous index

	dialogueArray = [
	("Please Enter A Name", 0)
	]

	# by moving the code within init to main
	# and removing self as a required paramater from clearScreen
	# game never needs to be initialised which might make the code more intuitive (idk)

	def __init__(self):

		self.screenUpdateScheduled = True
		self.screenHeight = 0
		self.screenWidth = 0

		game.terminalHeight = 0
		pygame.font.init()
		icon = pygame.image.load('icon.png')
		pygame.display.set_caption("Gal Game")
		pygame.display.set_icon(icon)

		game.screen = pygame.display.set_mode((900, 675), pygame.RESIZABLE)

		game.running = True

	def clearScreen(self):
		self.screen.fill((250, 245, 240))

	def updateScreen(self, terminal, script):

		terminal.line = 0

		# <Redrawing Frame>
		script.currentGirl.drawFrame(script.currentGirl.currentFrame)
		terminal.draw()
		terminal.loadCache()
		# </Redrawing Frame>

		self.screenHeight = game.screen.get_size()[1]
		self.screenWidth = game.screen.get_size()[0]
		self.screenUpdateScheduled = False

		pygame.display.flip()



class event:
	
	# an event type of 0 does nothing
	raised = 0
	
	def check():
		return event.raised
	
	def handle(raised):
		doAction = {
		0 : event.noAction()
		}
		
		doAction[raised]
	
	def noAction():
		return

	def halt():
		pass



class userIO:

	def __init__(self, script):

		self.script = script
		self.event = ""

		self.do = {
		# Game Events
		pygame.QUIT : self.quit,
		pygame.KEYDOWN : self.keydown,

		# Keypress Events
		pygame.K_RETURN : self.enterPress,
		pygame.K_BACKSPACE : self.backspacePress,
		"unspecifiedKeypress": self.updateCommand
		}

	def handle(self):

		self.events = pygame.event.get()

		for event in self.events:
			self.event = event
			if event.type in self.do: self.do[event.type]()

	def quit(self):

		game.running = False
		pygame.quit()

	def keydown(self):

		if self.event.key in self.do: self.do[self.event.key]()
		else: self.do["unspecifiedKeypress"]()

	def enterPress(self):

		self.script.halt = False
		self.script.run(game.command)
		game.command = ""

	def backspacePress(self):
		game.command = game.command[:-1]

	def updateCommand(self):
		game.command += self.event.unicode



class terminal:

	def __init__(self, game):
		self.game = game
		self.line = 0
		self.height = 0
		self.width = 400
		self.margine = 10
		self.lineHeight = 14
		self.cache = [("text", "format")]

	def draw(self):

		screenSize = self.game.screen.get_size()

		xPosition = (screenSize[0] - self.width)
		yPosition = self.margine
		width = self.width - self.margine
		height = screenSize[1] - self.margine * 2

		self.height = height

		terminal = pygame.Rect(xPosition, yPosition, width, height)

		pygame.draw.rect(self.game.screen, self.game.pink, terminal)

	def write(self, text, textFormat):

		linesInTerminal = int(self.height / self.lineHeight)
		if self.line == linesInTerminal:
			self.terminalCache = []

		font, size, color = textFormat
		my_font = pygame.font.SysFont(font, size)
		text_surface = my_font.render(text, True, color)
		innerMargine = 3
		xOrigin = (self.game.screen.get_size()[0] - self.width) + innerMargine
		yOrigin = self.margine + innerMargine + self.line * self.lineHeight
		terminalOrigin = (xOrigin, yOrigin)

		self.game.screen.blit(text_surface, (terminalOrigin))

		self.line += 1

	def loadCache(self):
		
		for entry in self.cache:
			self.write(entry[0], entry[1])



class protagonist:

	def __init__(self, name):
		self.name = name
		self.reputation = 0



class girl:

	# "girl" needs an instance of the class "game"
	# because "screen" is an attribute of the instance
	# not the class

	def __init__(self, game, terminal):

		self.game = game
		self.pointer = 0
		self.affection = 0
		self.terminal = terminal

		self.name = ""
		self.currentFrame = 0
		self.dialogueArray = ["dialogue", "end or continue"]
		self.imageLocation = ["location", "resolution", "scaler"]

	def advance(self, frmt):

		self.terminal.cache.append((self.dialogueArray[self.pointer][0], frmt))
		self.pointer += 1

		while self.dialogueArray[self.pointer][1] == 1:
			self.terminal.cache.append((self.dialogueArray[self.pointer][0], frmt))
			self.pointer += 1

	def drawFrame(self, frame):

		self.currentFrame = frame
		self.game.clearScreen()

		image = self.imageLocation[frame]
		scaledImage = (image[1][0] * image[2], image[1][1] * image[2])
		self.image = pygame.image.load(image[0])
		self.image = pygame.transform.scale(self.image, scaledImage)
		screenWidth = self.game.screen.get_size()[0]
		imageWidth = scaledImage[0]
		imageOrigin = (screenWidth - imageWidth) / 2
		imageCenterCoordinate = (screenWidth - (imageWidth + self.terminal.width)) / 2


		self.game.screen.blit(self.image, (imageCenterCoordinate, 0))
