# coding: utf-8
from sys import argv

script = argv[0]
print "=" * 10 + script + "=" * 10

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

print "We can just give the function numbers directly:\n" + "=" * 30 
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:\n" + "=" * 30
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:\n" + "=" * 30
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:\n" + "=" * 30
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "=" * 30 + "\n" + "Own function:" + "\n" + "=" * 30
print "Упращенная программа для расчета времени"
print "Из задачек для 4 класса про скорость, время и растояние \n" + "=" * 30

def time_counter(distance, speed):
	time = distance / speed
	print "Если двигаться со скоростью %d км/ч" % speed
	print "Растояние в %d км" % distance
	print "Можно проехать за: %d часа" % time

print "Напишите среднюю скорость движения:"
speed = int(raw_input("км/ч > "))
print "Напишите растояние:"
distance = int(raw_input("км > "))

time_counter(distance, speed)


