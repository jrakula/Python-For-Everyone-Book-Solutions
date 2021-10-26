##Write another program that prompts for a list of numbers
##as above and at the end prints out both the maximum and minimum of
##the numbers instead of the average.

total = 0
count = 0
numbersTuple = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        number = float(inp)
    except:
        print('Invalid input')
        continue
    numbersTuple.append(number)
    total = total + number
    count = count + 1
    

print(total, count, max(numbersTuple), min(numbersTuple))
