##This program counts the distribution of the hour of the day
##for each of the messages. You can pull the hour from the “From” line
##by finding the time string and then splitting that string into parts using
##the colon character. Once you have accumulated the counts for each
##hour, print out the counts, one per line, sorted by hour as shown below.
##
##python timeofday.py
##
##Enter a file name: mbox-short.txt
##04 3
##06 1
##07 1
##09 2
##10 3
##11 6
##14 1
##15 2
##16 4
##17 2
##18 1
##19 1


dic = dict()
fhand = open('mbox-short.txt')

for line in fhand:
    lineList = line.split()
    if len(lineList) < 2 or len(lineList) == 0:
        continue
    if lineList[0] == 'From':
        splitTime = lineList[5].split(':')
        if splitTime[0] not in dic:
            dic[splitTime[0]] = 1
        else:
            dic[splitTime[0]] += 1
    else:
        continue


lst = list()
for key, val in list(dic.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)
