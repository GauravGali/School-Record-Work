# count odd and even from user entered values

def oddeven(tup): # to seperate odd . even values
    odd = []
    even = []

    for i in tup: # finding odd and even
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    print('The Odd values are : ' , odd)
    print('The even values are : ' , even)

vals = []
n = int(input('Enter number of values : '))

for i in range(n): # getting values from user
    num = int(input('Enter a number : '))
    vals.append(num)

vals = tuple(vals)
oddeven(vals) # calling the function