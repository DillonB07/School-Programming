def update_file(file: str, quote: str):
    with open(file, 'a') as f:
        f.write(f'{quote}\n')

def read_file(file:str):
    with open(file, 'r') as f:
        for line in f:
            print(line)

for i in range(1,4):
    quote: str = input(f'Please enter quote {i}: ')
    update_file('my_quote.txt', quote)

read_file('my_quote.txt')
