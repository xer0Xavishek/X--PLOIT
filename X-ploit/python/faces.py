a = "Global Stuffs Earth"

def Bangladesh_f():
    a = "Bangladesh"
    def Khulna_f():
        nonlocal a # nonlocal means inside a = "Khulna"
        a = "Khulna"
        print(a)
    Khulna_f()
    print("Inside Bangladesh", a)

Bangladesh_f()




print("In the main: ", a) # Global a