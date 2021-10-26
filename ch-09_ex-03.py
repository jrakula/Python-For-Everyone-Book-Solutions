##Write a program to read through a mail log, build a
##histogram using a dictionary to count how many messages have come from
##each email address, and print the dictionary.
##
##Enter file name: mbox-short.txt
##{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
##'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
##'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
##'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
##'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
##'ray@media.berkeley.edu': 1}

dic = dict()

inp = input('Enter file name: ')
fhand = open(inp)
for line in fhand:
    lineList = line.split()
    if len(lineList) == 0:
        continue
    if lineList[0] == 'From':
        if lineList[1] not in dic:
            dic[lineList[1]] = 1
        else:
            dic[lineList[1]] += 1
    else:
        continue
print(dic)
