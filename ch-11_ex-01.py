##Write a simple program to simulate the operation of the
##grep command on Unix. Ask the user to enter a regular expression and
##count the number of lines that matched the regular expression:
##    
##$ python grep.py
##Enter a regular expression: ^Author
##mbox.txt had 1798 lines that matched ^Author
##
##$ python grep.py
##Enter a regular expression: ^Xmbox.txt had 14368 lines that matched ^X-
##
##$ python grep.py
##Enter a regular expression: java$
##mbox.txt had 4175 lines that matched java$

import re

count = 0

inp = input('Enter a regular expression: ')
inpExp = str(inp)

fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if re.findall(inpExp, line) > []:
        count += 1
        
print('mbox.txt had', count, 'lines that matched', inpExp)
