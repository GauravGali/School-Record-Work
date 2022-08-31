def Read(files:str):
    k = open(files)
    l = ''
    while True:
        check = k.readline()
        if check == '':
            break
        l += check

    return l

a = Read(input('Enter you file source => '))
print(a)
