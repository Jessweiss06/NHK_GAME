# In dialogue Arrays:
# 0 means the dialogue is finished
# 1 means the dialogue continues from the previous index

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

imageLocation = [
("Byoeimero_Yuokini\\NHK_Concept.png", (2480, 3508), 1/6)
]

# init requires an instance of the game class, initialised in main
# and an instance of the terminal class, initialised in main
# and the girl class (not an instance)

def init(game, terminal, girl):
	byoeimero = girl(game, terminal)
	byoeimero.dialogueArray = dialogueArray
	byoeimero.imageLocation = imageLocation
	byoeimero.name = "Byoeimero"

	return byoeimero
