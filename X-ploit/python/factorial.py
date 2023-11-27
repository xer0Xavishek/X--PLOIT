n = int(input("Enter the number: "))
f =n
r = 1

while f != 0 :
    r *= f 
    f -= 1
print("Factorial of",n,"is:",r)