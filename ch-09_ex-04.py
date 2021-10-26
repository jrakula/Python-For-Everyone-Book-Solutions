##Add code to the above program to figure out who has the
##most messages in the file. After all the data has been read
##and the dictionary has been created, look through the dictionary
##using a maximum loop to find who has
##the most messages and print how many messages the person has.
##
##Enter a file name: mbox-short.txt
##cwen@iupui.edu 5

##Enter a file name: mbox.txt
##zqian@umich.edu 195

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


maxValue = 0
for key in dic:
    if dic[key] > maxValue:
        maxValue = dic[key]
        maxKey = key
print(maxKey, maxValue)
