a = "Global Stuffs Earth"

def Bangladesh_f():
    a = "Bangladesh"#Level 1 local area
    def Khulna_f():
        nonlocal a # nonlocal means inside "Khulna" everyhing
        a = "Khulna"#Level 2 local area
        def KCC_f():
            nonlocal a # nonlocal means inside "KCC" everyhing
            a = "KCC Royal more"#Level 3 local area
            print(a)
        KCC_f()
        print(a)
    Khulna_f()
    print("Inside Bangladesh", a)

Bangladesh_f()#Local area




print("In the main: ", a) # Global a