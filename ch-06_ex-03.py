def count(string, letter):
    count = 0
    for index in string:
        if index == letter:
            count = count + 1
    return(count)

string = input('Enter a string: ')
letter = input('Select a letter to count: ')

print(count(string, letter))
            
