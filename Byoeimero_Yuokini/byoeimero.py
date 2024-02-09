
dialogueArray = [
("Hello Tatsuhiro", 0),
("I'm Byoeimero UWU", 1),

("", 0),
("", 0),
("", 0),
("", 0),
("", 0),
("", 0),
("", 0),
("", 0),
]

# init requires an instance of the game class, initialised in main
# and the girl class (not an instance)

def init(game, terminal, girl):
	byoeimero = girl(game, terminal)
	byoeimero.imageLocation = "Byoeimero_Yuokini\\NHK_Concept.png"
	byoeimero.imageResolution = (1690, 3508)
	byoeimero.imageScaler = 1/6
	byoeimero.name = "Byoeimero"
	byoeimero.dialogueArray = dialogueArray

	return byoeimero
