##Write a program that reads a file and prints the letters
##in decreasing order of frequency. Your program should convert all the
##input to lower case and only count the letters a-z. Your program should
##not count spaces, digits, punctuation, or anything other than the letters
##a-z. Find text samples from several different languages and see how
##letter frequency varies between languages. Compare your results with
##the tables at https://wikipedia.org/wiki/Letter_frequencies.
import string

count = 0
dic = dict()
lst = list()

fhand = open('checkcheck.txt')
for line in fhand:
    line = line.translate(str.maketrans('','',string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    wordsList = line.split()
    if len(wordsList) > 0:
        for word in wordsList:
            for letter in word:
                count += 1
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] += 1
    else:
        continue
print(dic)

for key, val in list(dic.items()):
    lst.append((key, val / count))

lst.sort()

for key, val in lst:
    print(val,key)
