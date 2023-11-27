def main():
    x= int(input("what's x ? "))
    if is_odd(x):
        print("ODD!")
    else:
        print("Even")

def is_odd(n):
    return True if n % 2 == 1 else False
#n % 2 == 0  or[] n>=2 n==] is the boolian expression so it is true  or false by default
def is_odd(n):
    return n % 2 == 0
    

main()
