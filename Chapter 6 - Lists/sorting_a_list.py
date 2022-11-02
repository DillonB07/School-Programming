import random
import time
from colors import Colors

def my_sort(data: list):
    sorted_data: list = []
    for _ in range(len(data)):
        temp = min(data)
        sorted_data.append(temp)
        data.remove(temp)
    return sorted_data

for _ in range(random.randint(1, 100)):
    data: list = [random.randint(1, 100) for _ in range(10)]
    print(Colors.RED + f'Original list: {data}')
    print(Colors.CYAN + f'Sorted list: {my_sort(data)}')
    print('---\n')
    time.sleep(0.5)
