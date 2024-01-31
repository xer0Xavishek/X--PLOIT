# import sys
# sys.stdout = open('c:/Users/avish/OneDrive/Documents/Workspace/code/knacksack/output.txt', 'w')
# sys.stdin = open('c:/Users/avish/OneDrive/Documents/Workspace/code/knacksack/input.txt', 'r')

def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smol=None
    for elem in in_list:
        if smol==None or elem<smol:
            smol= elem
    
    return smol

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2