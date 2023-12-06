""" [expression for item in iterable] """#list comprehension structure
""" [expression for item in iterable] """#list comprehension structure

""" item-->      is a variable that takes each value in the iterable one by one

epression--> is a Python expression that is calculated for each item .

iterable--> is a iterable object/range or collection of objects like list, tuple, set, dictionary, etc. """


(print("hell yeah")) for _ in range(5) #error

""" list=[for i in range(input("Enter the number of elements: ")): xxxxxxxxxxxxxxxxxxxxx
    list.append(int(input("Enter the element: ")))] xxxxxxxxxxxxxxxxxxxxx   #error
print(list) """

#Lets fix this
#list comprehension 
lst = [int(input("Enter the element: ")) for _ in range(int(input("Enter the number of elements: ")))]
print(lst)