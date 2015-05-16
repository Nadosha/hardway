# coding: utf-8
# в этом файле отображены все возможные логические операции 
print "=" * 30 + "\n" + "\tLOGIC help" + "\n" + "-" * 30

print """TERMS \n%s
		and
		or
		not
		!= (not equal)
		== (equal)
		>= (greater-than-equal)
		<= (less-than-equal)
		True
		False
	""" % ("-" * 30)

print "-" * 30 + "\nTRUTH TABLES\n" + "-" * 30

print """NOT 
    		not False		True
    		not True		False
    """

print """OR
		True or False		True
		True or True		True
		False or True		True
		False or False		False
	"""

print """AND
		True and False		False
		True and True		True
		False and True		False
		False and False		False
	"""

print """NOT OR
		not (True or False)	False
		not (True or True)	False
		not (False or True)	False
		not (False or False)	True
	"""

print """NOT AND
		not (True and False)	True
		not (True and True)	False
		not (False and True)	True
		not (False and False)	True
	"""

print """!=	
		1 != 0	True
		1 != 1	False
		0 != 1	True
		0 != 0	False
	"""

print """==	
		1 == 0	False
		1 == 1	True
		0 == 1	False
		0 == 0	True
	"""

print "(END)"