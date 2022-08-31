import pickle
'''
a=open("in1.dat","wb")
c="y"
d={}
while c=="y":
    r=input("Enter the rno:")
    n=input("Enter the name:")
    d['roll']=r
    d['name']=n
    pickle.dump(d,a)
    c=input("Enter your choice:(y/n).....")
a.close()
'''


a=open("in1.dat","rb")
try:
    while True:
        e=pickle.load(a)
        print(e)
except:
    a.close()


