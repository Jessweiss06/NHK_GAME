import classes as cl
from Byoeimero_Yuokini import byoeimero
from Misaki import misaki
from Rei import rei

class script:

	def __init__(self, game, terminal):

		self.currentGirl = ""

		self.byoeimero = byoeimero.init(game, terminal, cl.girl)
		self.rei = rei.init(game, terminal, cl.girl)
		self.misaki = misaki.init(game, terminal, cl.girl)

		terminal.cache = []

		self.pointer = 0
		self.halt = False
		self.script = open("scriptCode.py", "r").readlines()

	def advance(self, game):

		exec(self.script[self.pointer])
		if self.halt: return
		self.pointer += 1

	# run will be used for any developer commands

	def run(self, command):

		term = command.split()
		print(f"command {term}")
		if len(term) < 2: return

		classs = {
		"rei": self.rei,
		"misaki": self.misaki,
		"byoeimero": self.byoeimero
		}

		if term[1] not in classs:
			print("invalid command")
			self.pointer += 1
			return

		method = {
		"appraise": self.appraise(classs[term[1]])
		}

		if term[0] not in method:
			print("invalid command")
			self.pointer += 1
			return
		
		method[term[0]]

	# <Developer Commands>
	def appraise(self, girl):

		name = girl.name
		affection = girl.affection
		finalS = "s" if affection != 1 else ""

		apraisal = f"{name} has {affection} affection point{finalS}"
		girl.terminal.cache.append((apraisal, cl.game.format5))
	# </Developer Commands>
