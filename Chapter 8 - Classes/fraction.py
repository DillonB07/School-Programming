class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def print_fraction(self):
        print(f'\n{self.numerator}\n-\n{self.denominator}\n')

    def print_type(self):
        if self.denominator > self.numerator:
            print('Proper')
        elif self.numerator > self.denominator:
            print('Improper')
        else:
            print('Whole')

    def set_numerator(self, numerator: int = 0):
        self.numerator = numerator

    def set_denominator(self, denominator: int = 1):
        self.denominator = denominator

    def inverse(self):
        if self.numerator == 0: return
        self.denominator, self.numerator = self.numerator, self.denominator

frac_a = Fraction()
frac_b = Fraction(1,2)

print(frac_a.get_numerator())
print(frac_a.get_denominator())
frac_a.print_fraction()
frac_a.print_type()

frac_b.set_numerator(2)
frac_b.set_denominator(4)
frac_b.print_type()
frac_b.inverse()
frac_b.print_fraction()
