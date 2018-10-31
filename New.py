import json
import Proj

def new():
	print("Starting a new project...")
	# empty json object
	data = {}

	print("What is the name of this project?")
	answer = raw_input(">> ")
	# TODO: add confirmation
	print("Your project name is " + answer + ".\n")

	# empty project in json, to be filled
	data[answer] = []

	print("What type is this project?")
	print("1. Novel (50k+).")
	print("2. Novella. (20k-50k).")
	print("3. Short story (1k-20k).")
	print("4. Flash fiction (100-1k).")
	print("5. NaNoWriMo Novel (50k).")
	print("6. Other.")
	project = input(">> ")

	# empty variable to hold project type
	projType = ""

	done = True
	while done:
		if (project < 7 and project > 0):
			done = False
			projType = parseProject(project)
			# TODO: add confirmation
			print("Your project type is " + projType + ".\n")
		else:
			# TODO: stop string error
			print("Not a valid response. Try again.")
			project = input(">> ")

	if(project != 5):
		print("What type of tracker do you want to use?")
		print("1. Months.")
		print("2. Weeks.")
		print("3. Days.")
		l = input(">> ")

		done = True
		while done:
			if (project < 4 and project > 0):
				done = False
				length = parseLength(l)
				# TODO: add confirmation
				print("Your tracking type is " + length + ".\n")
			else:
				print("Not a valid response. Try again.")
				project = input(">> ")
		print("What would you like to track?")
		print("1. Words.")
		print("2. Scenes.")
		print("3. Chapters")
		print("4. Other")
		t = input(">> ")

		done = True
		while done:
			if (t < 5 and t > 0):
				done = False
				tracker = parseTracker(t)
				# TODO: add confirmation
				print("You will be tracking " + tracker + ".\n")
			else:
				print("Not a valid response. Try again.")
				project = input(">> ")
	else:
		length = "days"
		print("For NaNoWriMo, your tracking type is " + length + ".\n")

		tracker = "words"
		print("For NaNoWriMo, you will be tracking " + tracker + ".\n")


# function to return type of project	
def parseProject(t):
	if (t == 1):
		return "novel"
	elif (t == 2):
		return "novella"
	elif (t == 3):
		return "short"
	elif (t == 4):
		return "flash"
	elif (t == 5):
		return "nano"
	else:
		print("What type is your project?")
		return raw_input(">> ")

def parseLength(l):
	if (l == 1):
		return "months"
	elif (l == 2):
		return "weeks"
	else:
		return "days"

def parseTracker(t):
	if (t == 1):
		return "words"
	elif (t == 2):
		return "scenes"
	elif (t == 3):
		return "chapters"
	else:
		print("What will you be tracking?")
		return raw_input(">> ")

def save(data):
	with open('projects.json', 'w') as outfile:
		json.dump(data, outfile)