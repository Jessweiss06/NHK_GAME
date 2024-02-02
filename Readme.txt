Classes:
********
game:

	This class is for any event that is not caused
	by characters within the game. Things like drawing
	the screen, rendering text, prompting user input, etc.

protagonist:

	This class is for storing nescesarry player information
	such as character name, scores, reputation etc.

girl:

	This class is for the games NPCs it handles their
	dialogue, rendering, positioning etc.

Common Variables:
*****************
pointer:

	This variable is for indexing dialogueArrays

dialogueArray:

	This variable is for storing all possable dialogue
	options for any given class instance, in other words a
	it is an implepentation of a dialogue tree.

affection:

	This variable stores the players score with a given
	girl instance.

reputation:

	This variable stores the averagere of all affection
	scores. It determines how high the affection scores
	can get as well.

Methods:
********
apraise:

	This is a development tool to print a girl instance's
	data to the command line.