l=[1,"abc",2.5,True,23,[[15,16],2,3,4,5]]

print(l[5][0][1])


l=[20,1.9,1.8,17,16,15,1.4]
for i in range(0,len(l)):
    if type(l[i])==int:
        print(l[i],"is integer")
    elif type(l[i])==float:
        print(l[i],"is float")
        
l=[20,1.9,1.8,17,16,15,1.4]
for i in range (0,len(l)):
    print(type(l[i]))
    
    
    
even=0
odd=0

l=[20,1.9,1.8,17,16,15,1.4]
for i in range(len(l)):
    if l[i]%2==0:
        print(l[i],"is even")
        even+=l[i]
    else:
        print(l[i],"is odd")
        odd+=l[i]