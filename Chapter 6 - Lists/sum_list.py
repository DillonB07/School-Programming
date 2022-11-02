import random

def sum_list(data: list):
    sum = 0
    for i in data:
       sum += i

    return sum


data: list = [random.randint(1, 100) for _ in range(1, random.randint(1, 100))]

print(f'Original list: {data}')
print(f'Sum: {sum_list(data)}')
