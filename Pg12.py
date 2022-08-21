# Store lower to lower.txt , upper to upper.txt and others to others.txt


def seg(): # function to segregate upper , lower
    seged = {'lower' : [] , 'upper' : [] , 'others' : []}
    
    entries = int(input('Enter number of values to be entred : '))
    for i in range(entries): # segregator
        val = input('Enter a character : ')
        if val.islower() :
            seged['lower'].append(val)
        elif val.isupper():
            seged['upper'].append(val)
        else:
            seged['others'].append(val)

    return seged


value = seg()

# opening each file to save respective values
with open('lower.txt' , 'w') as fh: 
    fh.writelines(value['lower'])

with open('upper.txt' , 'w') as fh:
    fh.writelines(value['upper'])

with open('others.txt' , 'w') as fh:
    fh.writelines(value['others'])