import pygame

class game:

	pointer = 0

	# In dialogue Arrays:
	# 0 means the dialogue is finished
	# 1 means the dialogue continues to the next index

	dialogueArray = [
	("Please Enter A Name", 0)
	]

	def __init__(self):

		pygame.font.init()
		icon = pygame.image.load('icon.png')
		pygame.display.set_caption("Galge Game")
		pygame.display.set_icon(icon)

		self.screen = pygame.display.set_mode((900, 675), pygame.RESIZABLE)
		self.screen.fill((250, 245, 240))
		pygame.display.flip()

		self.running = True

	def renderText(self, text, position, font):
		my_font = pygame.font.SysFont(font, 45)
		text_surface = my_font.render(text, False, (0, 0, 0))
		self.screen.blit(text_surface, (position))
		pygame.display.flip()

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

	def draw(self, text):

		self.game.screen.fill((250, 245, 240))

		self.image = pygame.image.load(self.imageLocation)
		self.image = pygame.transform.scale(self.image, self.imageResolution)
		screenWidth = self.game.screen.get_size()[0]
		imageWidth = self.imageResolution[0]
		imageOrigin = (screenWidth - imageWidth) / 2

		# The code below is really janky
		# Don't forget to make a more elegant solution

		self.game.screen.blit(self.image, (imageOrigin - (imageWidth / 3), 0))
		pygame.display.flip()

		self.game.renderText(text, (imageOrigin + (imageWidth / 5) * 2, 50), "MS Ariel")