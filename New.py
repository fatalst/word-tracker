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

def save(data):
	with open('projects.json', 'w') as outfile:
		json.dump(data, outfile)