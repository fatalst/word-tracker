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
