count = 0
inp = input('Enter a file name: ')
fhand = open(inp)
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] == 'From':
        print(words[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')
