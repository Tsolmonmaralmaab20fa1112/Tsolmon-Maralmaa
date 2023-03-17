
# бодлого-4
import numpy as np

arr = np.arange(1, 1000)

divisible_arr = arr[(arr % 3 == 0) | (arr % 7 == 0)]


divisible_sum = np.sum(divisible_arr)

print(f"нийт нийлбэр: {divisible_sum}")

# бодлого-3
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]

max_age, min_age = get_max_min_key(data, 'age')
print(f'Maximum age: {max_age}')
print(f'Minimum age: {min_age}')

# бодлого-1

def print_stars(n):
    for i in range(n):
        print('*'*(i+1))
