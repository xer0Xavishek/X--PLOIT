n = int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n,"is Prime")
else:
    print(n,"is Not prime")
    
    
    
    
l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    n=l[i]
    c=0
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        print(n,"is Prime")
    else:
        print(n,"is Not prime")
  


for i in range(1,1001):
    n=i
    c=0
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        print(n,"is Prime")
        
        
        
l = ['Hello','World.',"I", "Love", "Python"]
new_l = []
for i in range(len(l)):
    if len(l[i])%2==0:
        new_l.append( l[i] )
print(new_l)

def check_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,"is Prime")
    else:
        print(n,"is Not prime")
        
        
        
  def return_prime_list(lst):
    primes = []
    for i in range(len(lst)):
        n=lst[i]
        c=0
        for j in range(1,n+1):
            if n%j==0:
                c+=1
        if c==2:
            primes.append( n )
    return primes


l = [1,2,3,4,5,6,7,8,9,10,11,12,423,123,234,456,123,7,4,2342,123,431,432]
x = return_prime_list(l)
print(x)

l = [1,2,3,4,5,6,7,8,9,10,11,12,423,123,234,456,123,7,4,2342,123,431,432]

for i in range(len(l)):
    check_prime(l[i])