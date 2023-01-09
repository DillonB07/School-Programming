"""
Check if a triangle is isosceles.
"""

def check_isosceles(length_one, length_two, length_three):
    """Check if the triangle is isosceles"""
    if (
        length_one == length_two or length_two == length_three or length_one == length_three
    ) and (
        length_one != length_two or length_two != length_three or length_one != length_three
    ):
        return "Isosceles Triangle"
    if length_one == length_two and length_two == length_three:
        return "Equilateral Triangle"
    return "Not an isosceles triangle"

if __name__ == '__main__':
    l1 = input("Length 1: ")
    l2 = input("Length 2: ")
    l3 = input("Length 3: ")
    print(check_isosceles(l1, l2, l3))
