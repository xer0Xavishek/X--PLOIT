import sys
sys.stdout = open('python/output.txt', 'w')
sys.stdin = open('python/input.txt', 'r')
n = int(input("Enter the number of terms in the series: "))
s = 0
i=1
j=1
k=5
while j<=n and k<=n:
    if i%2!=0:
        s=s+j
        j+=3
    else:
        s=s+k
        k+=5
        i+=1

print(f"The sum of the series is: {s}")