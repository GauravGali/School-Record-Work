import pickle


with open('/Users/gauravgali/Desktop/Sample.bin' , 'wb') as fh :
    d = {}
    while True:
        k = eval(input('Enter the key => '))
        v = eval(input('Enter the value => '))
        d[k] = v
        if (input('Do you want to continue......y/n')) == 'n':
            break
    print(d)
    pickle.dump( d , fh )

print(' --------------------------------------------------- ')
    
with open('/Users/gauravgali/Desktop/Sample.bin' , 'rb') as fh :
    
    srh = eval(input('Enter the value to be searched => '))
    new_d = {}
    asked = {}

    
    
    while True:
        try:
            new_d = pickle.load(fh)
        except:
            break

    for i in new_d:
        if i == srh:
            print('Record Found')
            asked[i] = srh
            print(asked)
        else:
            print('Record Not Found')
