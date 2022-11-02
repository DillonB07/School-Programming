def add_hello(data: list):
    data.append('Hello')
    return data

data: list = ['I', 'like', 'to', 'say']

print(f'Original: {data}')
print(f'New: {add_hello(data)}')
