# coding: utf-8
from sys import argv

script = argv[0] #в квадратных скобках указал порядковый номер объекта масива argv, подробности потом в разделе масивов
# для декроривания
print "=" * 10 + script + "=" * 10

# They name pieces of code the way variables name strings and numbers.
# They take arguments the way your scripts take argv.
# Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %s, arg2: %s" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

#this one just takes one argument
def print_one(arg1):
	print "arg1: %s" % arg1

def print_none():
	print "I got nothin'."

print "print_two"
print_two("Zed", "Shaw")
print "print_two_again"
print_two_again("Zed", "Shaw")
print "print_one"
print_one("First!")
print "print_none"
print_none()