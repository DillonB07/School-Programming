"""Test the isosceles.py program"""
import random
import unittest
from isosceles import check_isosceles

class Test_TestCheckIsosceles(unittest.TestCase): # NOQA
    """Test the isosceles.py program"""
    def test_same_sides(self):
        """Check if the correct response is returned when all sides are equal"""
        num  = random.randint(1, 100)
        self.assertEqual(check_isosceles(num,num,num), "Equilateral Triangle")

    def test_first_two(self):
        """Check if the correct response is returned when the first two lengths are equal"""
        num  = 56
        num2 = 44
        self.assertEqual(check_isosceles(num,num,num2), "Isosceles Triangle")

    def test_last_two(self):
        """Check if the correct response is returned when the last two lengths are equal"""
        num  = 56
        num2 = 44
        self.assertEqual(check_isosceles(num,num2,num2), "Isosceles Triangle")

    def test_surrounding_two(self):
        """Check if the correct response is returned when the first and last lengths are equal"""
        num  = 56
        num2 = 44
        self.assertEqual(check_isosceles(num,num2,num), "Isosceles Triangle")

    def test_invalid(self):
        """Check if the correct response is returned when none of the lengths are equal"""
        num  = 56
        num2 = 44
        num3 = 68
        self.assertEqual(check_isosceles(num,num2,num3), "Not an isosceles triangle")

if __name__ == '__main__':
    unittest.main()
