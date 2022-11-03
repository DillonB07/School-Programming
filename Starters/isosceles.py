"""
Check if a triangle is isosceles.
"""

length_one = input('Length 1: ')
length_two = input('Length 2: ')
length_three = input('Length 3: ')

if (length_one == length_two or length_two == length_three or length_one == length_three) and (length_one != length_two or length_two != length_three or length_one != length_three):
    print('Isosceles Triangle')
else:
    print("Not an isosceles triangle")
