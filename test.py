# coding: utf-8
points = 0
lifes = 3

def question():
	while True:
		print "Score: %d  Lifes: %d" % (points, lifes)
		print "Texet question here"
		answer = raw_input("> ")
		if answer == "a":
			print "Greating! your count"
			count(True)
		elif answer == "b":
			print "Sad"
			count(False)
		else:
			print "Try once more"

def count(answer):
	global points
	global lifes
	if answer:
		points += 5
		return points
	elif not answer:
		lifes -=1
		if lifes <= 0:
			print "GemeOver"
			exit(0)
		else:
			return lifes
	else:
		"ERROR!"			

question()
