## Write a function called chop that takes a list and modifies
##it, removing the first and last elements, and returns None.

##Then write a function called middle that takes a list and returns a new list
##that contains all but the first and last elements.

def chop(aList):
    del aList[0]
    del aList[-1]

def middle(aList2):
    lst = []
    for item in aList2:
        lst.append(item)
    del lst[0]
    del lst[-1]
    return lst

myList1 = [1, 2, 3, 4]
myList2 = [1, 2, 3, 4]

chopList = chop(myList1)
print(myList1)
print(chopList)


middleList = middle(myList2)
print(myList2)
print(middleList)
