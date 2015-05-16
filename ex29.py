# coding: utf-8
from sys import argv
script = argv[0]
print "=" * 10 + script + "=" * 10

people = 40 
cats = 30 
dogs = 15

if people < cats:
	print "To many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater that or equal to dogs."

if people <= dogs:
	print "People are less that or equal to dogs."

if people == dogs:
	print "People are dogs."

#Stady Drill - own  boolean expression:
cats -= 15
print "My own  boolean expressions"
print "-" * 30 
if people > dogs > cats:
	print "People are awsome"
	if dogs > cats:
		print "And dogs cool too!"