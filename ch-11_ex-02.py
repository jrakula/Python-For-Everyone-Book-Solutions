##Write a program to look for lines of the form:
##New Revision: 39772
##
##Extract the number from each of the lines using a regular expression
##and the findall() method. Compute the average of the numbers and
##print out the average as an integer.
##
##Enter file:mbox.txt
##38549
##
##Enter file:mbox-short.txt
##39756

import re
count = 0

inp = input('Enter file: ')
fhand = open(inp)

for line in fhand:
    line = line.rstrip()
    if re.findall(^New Revision:, line) > []:
        count += 1
