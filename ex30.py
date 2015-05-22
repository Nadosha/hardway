people = 20
cars = 45
trucks = 30

if cars > people:
	print "We shoukd take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We van't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print  "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

print "-" * 30
if not(people != trucks and trucks - cars == people or True):
	print "If statements True"
elif trucks + people < people + cars:
	print "elif statement True"
else:
	print "else statement"