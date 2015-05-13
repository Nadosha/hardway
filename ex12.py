# coding: utf-8
ex = "ex12.py"
print "=" * 10 + ex + "=" * 10

age = int(raw_input("How old are you? ")) # Принимает аргумент и выводит его в терминале
height = int(raw_input("How tall are you? "))
weight = int(raw_input("How much do you weight? "))

print "So, you're %d old, %d tall and %d heavy." % (age, height, weight)