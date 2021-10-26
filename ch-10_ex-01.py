## Revise a previous program as follows: Read and parse the
##“From” lines and pull out the addresses from the line. Count the
##number of messages from each person using a dictionary.
##After all the data has been read, print the person with the most commits
##by creating a list of (count, email) tuples from the dictionary. Then
##sort the list in reverse order and print out the person who has the most
##commits.
##
##Sample Line:
##From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
##
##Enter a file name: mbox-short.txt
##cwen@iupui.edu 5

##Enter a file name: mbox.txt
##zqian@umich.edu 195


dic = dict()
fhand = open('mbox-short.txt')

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
print(list(dic.items()))
print(' ')
print(dic)
print(' ')

lst = list()
for key, val in list(dic.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:1]:
    print(val, key)
