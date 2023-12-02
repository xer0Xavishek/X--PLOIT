a = "Global a"

def outer_f():
    a = "Outer a(local)"
    def inner_f():
        nonlocal a
        a = "Inner a(nonlocal)"
        print("Inside inner_f(): ", a)
    inner_f()
    print("Inside outer_f(): ", a)

outer_f()
print("In the main: ", a)