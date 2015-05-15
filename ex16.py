# coding: utf-8
from sys import argv
script, filename = argv

print "=" * 10 + script + "=" * 10

#++++| Теория |++++
# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("=" * 10 + script + "=" * 10 + "\n") # тут все не так как в упражнении
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.write("=" * 12 + "END" + "=" * 12)

print "Saving..."
target.close()

txt = open(filename)
print txt.read()