import classes as cl
from Byoeimero_Yuokini import byoeimero
from Rei import rei

class script:

	def __init__(self, game):

		self.byoeimero = byoeimero.init(game, cl.girl)
		self.rei = rei.init(game, cl.girl)

		game.terminalCache = []

		self.pointer = 0
		self.script = [
		(self.byoeimero, cl.game.format2),
		(self.rei, cl.game.format3)
		]

	def advance(self, game):

		self.script[self.pointer][0].advance(self.script[self.pointer][1])
		self.pointer += 1

	def update(self):

		self.rei.drawFrame()
