# coding: utf-8
from sys import argv 
script , first, second, third = argv 

print "=" * 10 + script + "=" * 10 # декорирование спомошью импорта модуля argv
# argv - принимает аргумент введенный перед запуском скрипта в терминале
# ~ python ex13.py script[аргумен1], [аргумен2] ...

print "The script is called: ", script # это название перемнной, может быть любым словом
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your thirdvariable is: ", third
