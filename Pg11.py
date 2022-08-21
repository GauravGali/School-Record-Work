# Write a Python program to implement a stack using list.

def Insert(lis):
    val = eval(input('Enter the value you want to insert : ')) 
    pos = int(input('Enter the position to insert the value : '))
    lis.insert(pos-1 , val)
    print('The Updated List : ' , lis)

def Delete(lis):
    val = eval(input('Enter the value you want to delete : ')) 
    try:
        lis.remove(val)
        print('The Updated List : ' , lis)
    except:
        print(f'{val} in not present in the list')
        print('The List was unchanged : ' , lis)

def Update(lis):
    val = eval(input('Enter the value you want to update with : ')) 
    lis.append(val)
    print('The Updated List : ' , lis)

def Traverse(lis):
    pos = int(input('Enter the position to find the value : '))
    try:
        print(f'The value at {pos} position : ' , lis[pos-1])
    except:
        print(f'OOPS there is not value at {pos} position !')

def Merge(lis):
    newLis = eval(input('Enter the new List to merge : '))
    lis += newLis

    print('The Updated List : ' , lis)


conditions = """
    1 To Insert a Item
    2 To Delete a Item
    3 To Update a Item
    4 To Search a Item
    5 To Merge  a Item
    6 To Show   a List
    7 To End
"""

l = []

while True:
    print(conditions)

    cond = int(input('Enter your option : '))

    if cond == 1:
        Insert(l)
    elif cond == 2:
        Delete(l)
    elif cond == 3:
        Update(l)
    elif cond == 4:
        Traverse(l)
    elif cond == 5:
        Merge(l)
    elif cond == 6:
        print(l)
    elif cond == 7:
        print('Process Ended')
        break
    else:
        print('Invalid Entry ! Instead Try : ')