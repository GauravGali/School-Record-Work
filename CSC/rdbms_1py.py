def push(s,v):
    s.append(v)
    top=len(s)-1

def Pop(s):
    if len(s)==0:
        return "Underflow"
    else:
        d=s.pop()
        top=len(s)-1
        return d

def peek(s):
    if len(s)==0:
        return "Underflow"
    else:
        top=len(s)-1
        return s[top]
def display(s):
    if len(s)==0:
        print("Stack is empty")
    else:   
        top=len(s)-1
        print(s[top],"<--TOP")
        for i in range(top-1,-1,-1):
            print(s[i])
        
    
    
s=[]
while True:
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    c=int(input("Enter the choice:"))
    if c==1:
        item=eval(input("Enter the item to be pushed:"))
        push(s,item)
        print("value inserted successfully")
    elif c==2:
        f=Pop(s)
        if f=="Underflow":
            print("Stack is empty")
        else:
            print("The deleted item is :",f)
    elif c==3:
        p=peek(s)
        if p=="Underflow":
            print("Stack is empty")
        else:
            print("the top most element is :",p)
    elif c==4:
        display(s)
    elif c==5:
        break
    else:
        pass
