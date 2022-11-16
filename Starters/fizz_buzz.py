"""Program to play the Fizzbuzz game."""

def check_prime(val: int):
    """Check if a number is prime."""
    if val > 1:
        for k in range(2, int(val / 2) + 1):
            if val % k == 0:
                return False
            break
        else:
            return True

num = int(input("Enter a number: "))
first_base = input("Enter the first base: ")
second_base = input("Enter the second base: ")

if first_base == "":
    BASE_ONE = 3
else:
    BASE_ONE = int(first_base)
if second_base == "":
    BASE_TWO = 5
else:
    BASE_TWO = int(second_base)

for i in range(1, num + 1):
    if check_prime(i) is True:
        print(f"{i} - Oops!")
    elif i % BASE_ONE == 0 and i % BASE_TWO == 0:
        print(f"{i} - FizzBuzz")
    elif i % BASE_ONE == 0:
        print(f"{i} - Fizz")
    elif i % BASE_TWO == 0:
        print(f"{i} - Buzz")
    else:
        print(i)
