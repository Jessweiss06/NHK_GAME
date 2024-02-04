import classes as cl

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

def init(game):
	byoeimero = cl.girl(game)
	byoeimero.imageLocation = "Byoeimero_Yuokini\\NHK_Concept.png"
	byoeimero.imageResolution = (1690, 3508)
	byoeimero.imageScaler = 1/6
	byoeimero.name = "Byoeimero"
	byoeimero.dialogueArray = dialogueArray

	return byoeimero