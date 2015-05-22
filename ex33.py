# coding: utf-8
from sys import argv
script = argv[0]
print "=" * 10 + script + "=" * 10


numbers = []

def count(x):

	print "Function numbers"
	i = 0

	while i <= x:
		print "At the top i is %d" % i 
		numbers.append(i)

		i += 3
		print "Numers now: ", numbers
		print "At the bottom i is %d" % i

limit = count(int(raw_input("> ")))

print "The numbers: "

for num in numbers:
	print num