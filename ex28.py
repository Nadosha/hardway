True and True  #True +
False and True #False +
1 == 1 and 2 == 1  #False +
"test" == "test" #True +
1 == 1 or 2 != 1 #True +
True and 1 == 1 #True +
False and 0 != 0 #False +
True or 1 == 1 #True +
"test" == "testing" #False +
1 != 0 and 2 == 1 #False +
"test" != "testing" #True +
"test" == 1 #False +
not (True and False) # разбор: not (True and False) => not (False) => True +
not (1 == 1 and 0 != 1) # => not (True and True) => not (True) => False +
not (10 == 1 or 1000 == 1000) # =>not(False or True) => not (True) => False +
not ( 1 != 10  or 3 == 4) # =>not(True or False) => not(True) => False +
not ("testing" == "testing" and "Zed" == "Cool Guy") 
# => not(True and False) => not(False) => True +
1 == 1 and (not("testing" == 1 or 1 == 0))
# => True and not(False or False) =>True and not(False) => True and True => True -
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) 
# => False and (not(False or True)) => False and (not(True)) => False and False => False +
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
# => True and (not(True or False)) => True and (not(True)) => True and False => False -

#Study Drill - my booleans
one = 4 <= 5 and True or (not("Python" == "Python" or 2 >= 2 and False))
# True and True or (not(True or True and False)) => True and True or (not(False)) =>True and True => True +
not(True == one or 1 != 5) and 2 == 2
# not(True or True) and True = False and True => False + 
#теория с книги:
"""
1. Solve each equality test:

	3 != 4 is True: True and not ("testing" != "test" or "Python" == 
	"Python") "testing" != "test" is True: True and not (True or 
	"Python" == "Python") "Python" == "Python": True and not (True or True)

2. Find each 'and/or' in parentheses ():

	(True or True) is True: True and not (True)

3. Find each 'not' and invert it:

	not (True) is False: True and False

4. Find any remaining 'and/or' and solve them:

	True and False is False
"""