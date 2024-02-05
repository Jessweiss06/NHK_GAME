
dialogueArray = [
("Hey Tatsuhiro!", 0),
("It's Rei", 1),
("", 0),
("", 0)
]

def init(game, girl):
	rei = girl(game)
	rei.imageLocation = "Rei\\NHK_Concept.png"
	rei.imageResolution = (817, 3508)
	rei.imageScaler = 1/6
	rei.name = "Rei"
	rei.dialogueArray = dialogueArray

	return rei