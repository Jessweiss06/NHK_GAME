
dialogueArray = [
("Hey! You're one hour late.", 0),
("Did you bring the contract?", 1),
("What does object-oriented programming mean?", 2),
("", 0)
]

# init requires an instance of the game class, initialised in main
# and the girl class (not an instance)

def init(game, terminal, girl):
	misaki = girl(game, terminal)
	misaki.imageLocation = "Misaki\\holdingContract.jpg"
	misaki.imageResolution = (1024, 1024)
	misaki.imageScaler = 14/20
	misaki.name = "Misaki"
	misaki.dialogueArray = dialogueArray

	return misaki
