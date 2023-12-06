""" [expression for item in iterable] """#list comprehension structure

""" item-->      is a variable that takes each value in the iterable one by one

epression--> is a Python expression that is calculated for each item .

iterable--> is a iterable object/range or collection of objects like list, tuple, set, dictionary, etc. """



# You can add if condition to the list comprehension
even_squares = [(x**2) for x in range(10) if (x % 2 == 0)]

print(even_squares)  # Output: [0, 4, 16, 36, 64]


#Lets fix this
#list comprehension 
lst = [int(input("Enter the element: ")) for _ in range(int(input("Enter the number of elements: ")))]
print(lst)