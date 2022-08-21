# odd to 2x and even to 0.5x

def o2xe0p5x(lis): # converts odd to 2x and even to 0.5x
    new = []

    print('The Given List : ' , lis)

    for i in lis:
        if i % 2 == 0:
            new.append(int(i*0.5))
        else:
            new.append(i*2)
    
    print('The Updated List : ' , new)

n = int(input('Enter the number of values to be entered :'))
l = []

for i in range(n): #getting user inputs
    val = int(input('Enter a number : '))
    l.append(val)

o2xe0p5x(l) # calling the function