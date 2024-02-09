import classes as cl
from Byoeimero_Yuokini import byoeimero
from Rei import rei

class script:

	def __init__(self, game, terminal):

		self.byoeimero = byoeimero.init(game, terminal, cl.girl)
		self.rei = rei.init(game, terminal, cl.girl)

		terminal.cache = []

		self.pointer = 0
		self.halt = False
		self.script = open("scriptCode.py", "r").readlines()

	def advance(self, game):

		exec(self.script[self.pointer])
		if self.halt: return
		self.pointer += 1

	def update(self):

		self.rei.drawFrame()
