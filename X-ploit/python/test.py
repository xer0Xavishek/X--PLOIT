N=int(input())
sum=0
for i in range(1,N+1,1):
  if i%7==0 or i%9==0:
    sum=sum+i
  elif i%7==0 and i%9==0:
    sum=sum+0
  elif i%7!=0 or i%9!=0:
    continue
print(sum)