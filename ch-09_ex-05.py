##This program records the domain name (instead of the
##address) where the message was sent from instead of who the mail came
##from (i.e., the whole email address). At the end of the program, print
##out the contents of your dictionary.
##
##python schoolcount.py
##Enter a file name: mbox-short.txt
##{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
##'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

dic = dict()

inp = input('Enter file name: ')
fhand = open(inp)
for line in fhand:
    lineList = line.split()
    if len(lineList) == 0:
        continue
    if lineList[0] == 'From':
        splitAddress = lineList[1].split('@')
        if splitAddress[1] not in dic:
            dic[splitAddress[1]] = 1
        else:
            dic[splitAddress[1]] += 1
    else:
        continue
print(dic)
