fh = open('sv.txt' , 'a')
fh.write('Vikram \n')
a = input('Enter smtg => ')
fh.write(a)
fh.flush()
s = 'sv rocks'
k = {'a':'hello \n' , 'b':'all \n' }
fh.writelines(k)
fh.write(s)
fh.flush()
