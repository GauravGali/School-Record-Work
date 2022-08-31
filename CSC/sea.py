import pickle
a=open("in1.dat","rb")
val=input("Enter the name to be changed:")
l = []
try:
    while True:
        p=a.tell()
        e=pickle.load(a)
        l.append( e )
        '''
        if e['name']==val:
            e['name']="Anish"
            a.seek(p,0)
            pickle.dump(e,a)
        '''
    
    
except:
    a.close()
    
for i in l:
    if i['name'] == val:
        i['name'] = 'Gaurav'

k = open('in1.dat' , 'wb')
pickle.dump(l ,k)
k.close()
