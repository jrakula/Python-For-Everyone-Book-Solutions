wordList = list()
fhand = open(input('Enter file: '))
for line in fhand:
    words = line.split()
    for word in words:
        if word in wordList:
            continue
        else:
            wordList.append(word)
print(sorted(wordList))
