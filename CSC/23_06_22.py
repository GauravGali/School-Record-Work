import pickle
'''a=open("text.bin","wb")
n=10
f=10.5
s="grade12"
l=[1,2,3,4]
t=(1,2,"tuple")
d={1:100,2:200}
pickle.dump(n,a)
pickle.dump(f,a)
pickle.dump(s,a)
pickle.dump(l,a)
pickle.dump(t,a)
pickle.dump(d,a)
a.close()'''

a=open("text.bin","rb")
while True:
    try:
        print(pickle.load(a))
    except:
        a.close()
    
