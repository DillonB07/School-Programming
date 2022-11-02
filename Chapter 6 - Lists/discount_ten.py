import random

def discount_ten(data: list):
    for i in data:
        discount: float = i / 10
        data[data.index(i)] = round(i - discount, 2)

    return data


data: list = [round(random.randint(1,30)*random.random(), 2) for _ in range (1,10)]
print(f'Original list: {data}')

print(f'New data: {discount_ten(data)}')
