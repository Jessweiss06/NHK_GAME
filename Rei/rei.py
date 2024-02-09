
dialogueArray = [
("Hey Tatsuhiro!", 0),
("It's Rei", 1),
("", 0),
("", 0)
]

# init requires an instance of the game class, initialised in main
# and the girl class (not an instance)

def init(game, terminal, girl):
	rei = girl(game, terminal)
	rei.imageLocation = "Rei\\NHK_Concept.png"
	rei.imageResolution = (817, 3508)
	rei.imageScaler = 1/6
	rei.name = "Rei"
	rei.dialogueArray = dialogueArray

	return rei
