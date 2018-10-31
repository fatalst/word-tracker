import New
import Proj

def initialize():
	print("Welcome to the word tracker!")
	print("1. Start a new project.")
	print("2. Open an old project.")
	print("3. Exit.")
	response = input(">> ")
	done = True

	while done:
		if(response == 1):
			done = False
			New.new()
		elif(response == 2):
			done = False
			Proj.load()
		elif(response == 3):
			done = False
			quit()
		else:
			# TODO: stop string error
			print("Not a valid response. Try again.")
			response = input(">> ")