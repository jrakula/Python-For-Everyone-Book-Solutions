##Write a while loop that starts at the last character in the
##string and works its way backwards to the first character in the string,
##printing each letter on a separate line, except backwards.
strInput = str(input('Input a string: '))
index = 0 - len(strInput)
start = -1
while start >= index:
    print(strInput[start])
    start -= 1
