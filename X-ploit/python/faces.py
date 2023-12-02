a = "Global Stuffs Earth"

def Bangladesh_f():
    a = "Bangladesh"#Level 1 local area
    def Khulna_f():
        nonlocal a # nonlocal means inside a = "Khulna"
        a = "Khulna"#Level 2 local area
        print(a)
    Khulna_f()
    print("Inside Bangladesh", a)

Bangladesh_f()#Local area




print("In the main: ", a) # Global a