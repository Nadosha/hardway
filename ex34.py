#coding: utf-8
from sys import argv
script = argv[0]
print "=" * 10 + script + "=" * 10

# Example from exercise
animals = ['bear', 'fish', 'python', 'kangaroo', 'whale', 'bird']
array = []
count = []
i = -1
y = 0

for index in animals:
	i += 1
	y += 1
	array.append(i)
	count.append(y)
	print "The animal at %d is the %dst animal and is a %s. " % (i, y, index)
