# coding: utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "=" * 10 + script + "=" * 10 + "\n"

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

# How it can be realized in one line:
out_file = open(from_file, 'r').read(); in_file = open(to_file, 'w').write(out_file)

print "The input file is %d bytes long" % len(out_file)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)


print "Alright, all done."

#out_file.close()
#in_file.close()



