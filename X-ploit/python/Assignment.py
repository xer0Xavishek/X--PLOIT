# Open the input file and read the lines
f = open('arr_info.txt', 'r')
lines = f.readlines()
f.close()

# Split each line into a list of numbers
numbers = []
for line in lines:
    numbers.append(list(map(int, line.split('-'))))

# Sum the numbers in each column
sums = []
for i in range(len(numbers[0])):
    column_sum = 0
    for row in numbers:
        column_sum += row[i]
    sums.append(column_sum)

# Convert the sums to strings and join them with hyphens
output = ''
for sum in sums:
    output += str(sum) + '-'
output = output[:-1]  # Remove the trailing hyphen

# Write the output to the output file
f = open('arr_out.txt', 'w')
f.write(output)
f.close()