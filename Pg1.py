# linear search , frequency , position of element

def search(lis): # searching the list
    print(lis)
    val = eval(input('Enter the value to be searched : '))
    frequency = lis.count(val)
    pos = []

    for i in range(len(lis)):
        if val == lis[i]:
            pos.append(i+1) 
    

    print(f'The frequency of {val} is {frequency}')
    print('List Of Values : ' , lis)
    print('The positions  : ' , pos)


n = int(input('Enter the number of values to be entered :'))
l = []

for i in range(n): #getting user inputs
    val = int(input('Enter a number : '))
    l.append(val)

search(l)