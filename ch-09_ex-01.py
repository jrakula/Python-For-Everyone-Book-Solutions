##Write a program that reads the words in words.txt and stores them as
##keys in a dictionary. It doesn’t matter what the values are. Then you
##can use the in operator as a fast way to check whether a string is in the
##dictionary
dic = dict()
count = 0
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        lowerWord = word.lower()
        if lowerWord not in dic:
            dic[lowerWord] = count
            count = count + 1


inp = input('Enter a word to check if it is in words.txt: ')
lowerInp = inp.lower()
if lowerInp in dic:
    print(lowerInp, 'is in text')
else:
    print(lowerInp, 'is not in text')
    
