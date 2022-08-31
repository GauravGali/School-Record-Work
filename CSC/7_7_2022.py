import pickle

with open('sample.dat' , 'wb') as fh :
    inp = int(input('Enter number of records : '))
    d = {}
    for i in range(inp):
        name = input('Enter the name : ')
        roll = input('Enter the roll no : ')
        d[name] = roll
        pickle.dump(d , fh)

with open('sample.dat' , 'rb') as fh :
    k = pickle.load(fh)
    print(k)
