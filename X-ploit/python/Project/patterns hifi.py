n = 5  # Change this value to set the size of the butterfly

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    spaces = 2 * (n - i)
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    spaces = 2 * (n - i)
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

n = 5 # Change this value to set the number of rows

for i in range(1, n + 1):
    for j in range(1, i+1):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the hourglass

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

    n = 5  # Change this value to set the number of rows

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
n = 5  # Change this value to set the size of the pyramid

for i in range(1, n + 1):
    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    # Print stars
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()

n = 5  # Change this value to set the size of the triangle

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

n = 5  # Change this value to set the size of the square

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the diamond

# Print the top half of the diamond
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

# Print the bottom half of the diamond
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

n = 5  # Change this value to set the size of the rhombus

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

n = 5  # Change this value to set the size of the diamond

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(j + 1, end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(j + 1, end=" ")
    print()

rows = 4  # Change this value to set the number of rows
cols = 6  # Change this value to set the number of columns

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the inverted pyramid

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

n = 5  # Change this value to set the size of the triangle

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 6  # Change this value to set the size of the arrow

for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        if j == 0 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the diamond

start_char = ord('A')

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(chr(start_char + j), end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(chr(start_char + j), end=" ")
    print()

n = 5  # Change this value to set the number of rows

for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if i == j:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
#spiral pTTERN
n = 4  # Change this value to set the number of rows and columns

matrix = [[0 for _ in range(n)] for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
row, col = 0, 0

for i in range(1, n * n + 1):
    matrix[row][col] = i
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]
    if (
        0 <= new_row < n
        and 0 <= new_col < n
        and matrix[new_row][new_col] == 0
    ):
        row, col = new_row, new_col
    else:
        direction = (direction + 1) % 4
        row, col = row + directions[direction][0], col + directions[direction][1]

for row in matrix:
    for num in row:
        print(f"{num:2}", end=" ")
    print()

n = 5  # Change this value to set the size of the rhombus

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the inverted pyramid

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        if i == n or j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # Change this value to set the size of the X pattern

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#half pyramid
n = 5  # Change this value to set the size of the half-pyramid

start_char = ord('A')

for i in range(1, n + 1):
    for j in range(i):
        print(chr(start_char + j), end=" ")
    print()

#butterfly
n = 5  # Change this value to set the size of the butterfly

start_char = ord('A')

for i in range(n):
    for j in range(i + 1):
        print(chr(start_char + j), end=" ")
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        if j == n:
            continue
        print(chr(start_char + j), end=" ")
    print()
#cristmas tree
n = 7  # Change this value to set the size of the Christmas tree

for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
    
# Print the trunk
trunk_height = n // 2
for i in range(trunk_height):
    spaces = n - 1
    print(" " * spaces + "||")
#heart
n = 6  # Change this value to set the size of the heart

for i in range(n // 2, n + 1, 2):
    print(" " * (n - i), end="")
    print("*" * i, end="")
    print(" " * (n - i), end="")
    print("*" * i)

for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(" ", end="")
    print("*" * (2 * i - 1), end="")
    print()
#diamond with special character
n = 5  # Change this value to set the size of the diamond

special_chars = ["@", "#", "$", "%", "&", "*", "?", "!", "~", "+"]

for i in range(n):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print(special_chars[i], end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print(special_chars[i], end=" ")
    print()
#chessboard
n = 8  # Size of the chessboard

for i in range(n):
    for j in range(n):
        # Check if the sum of row and column indices is even
        if (i + j) % 2 == 0:
            print("█", end=" ")  # Use a filled square or any other character for black squares
        else:
            print(" ", end=" ")  # Use a space for white squares
    print()
