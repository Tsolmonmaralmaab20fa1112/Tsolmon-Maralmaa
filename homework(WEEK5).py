# Problem1
numbers = [i for i in range(50, 101)]

print(numbers)

# Problem2
ones = [1 for i in range(10)]

print(ones)

zeros = [0 for i in range(10)]

print(zeros)

sixs = [6 for i in range(10)]

print(sixs)

# Problem3
massive3 = []

for i in range(3):
    row = []
    for j in range(4):
        num = 20 + i*4 + j
        row.append(num)
    massive3.append(row)

print(massive3)

# Problem4
massive4 = []
for i in range(3):
    row = []
    for j in range(3):
        if i == j == 1:
            row.append(1)
        else:
            row.append(0)
    massive4.append(row)

print(massive4)

# Problem5
massive5 = []
for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(i+1)
        else:
            row.append(0)
    massive5.append(row)

print(massive5)

# Problem6
import numpy as np

massive6 = np.random.randint(1, 11, size=(4, 3))

print("Matrix:\n", massive6)

row_sums = massive6.sum(axis=1)
col_sums = massive6.sum(axis=0)
total_sum = massive6.sum()

# Print the sums
print("Row sums:", row_sums)
print("Column sums:", col_sums)
print("Total sum:", total_sum)