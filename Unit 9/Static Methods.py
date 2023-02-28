class Fraction:
    def __init__(self, n, d): 
        self.num = n
        self.den = d
    
    @staticmethod # function decorator
    def product(f1,f2):
        final_product = Fraction(f1.__num*f2.__num,f1.__den*f2.__den)
        return final_product

    @staticmethod # function decorator
    def absolute(f1):
        final_absolute = Fraction(abs(f1.num), abs(f1.den))
        return final_absolute
    
    @staticmethod # function decorator
    def is_positive(f1):
        if f1.num > 0:
            return True
        else:
            return False