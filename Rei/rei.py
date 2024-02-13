# In dialogue Arrays:
# 0 means the dialogue is finished
# 1 means the dialogue continues from the previous index

dialogueArray = [
("Hey Tatsuhiro!", 0),
("It's Rei", 1),
("", 0),
("", 0)
]

imageLocation = [
("Rei\\NHK_Concept.png", (817, 3508), 1/6)
]

# init requires an instance of the game class, initialised in main
# and an instance of the terminal class, initialised in main
# and the girl class (not an instance)

def init(game, terminal, girl):
	rei = girl(game, terminal)
	rei.dialogueArray = dialogueArray
	rei.imageLocation = imageLocation
	rei.name = "Rei"

	return rei
