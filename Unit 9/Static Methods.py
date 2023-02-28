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

def user_input(): 
    while True:
        try: 
            f1_num = float(input("Enter the numerator for f1: ")) 
            f1_den = float(input("Enter the denominator for f1: ")) 
            f2_num = float(input("Enter the numerator for f2: "))
            f2_den = float(input("Enter the denominator for f2: ")) 
            if f1_den != 0 or f2_den != 0: 
                return f1_num, f1_den, f2_num, f2_den
            else: 
                print("Please enter a proper denominator (not equal to 0)")
        except:
            print("Please enter an integer")

def start():
    inputs = user_input()

    print("Fraction 1")
    f1 = Fraction(inputs[0], inputs[1])
    f1.num = inputs[0]
    f1.den = inputs[1]

    print("Fraction 2")
    f2 = Fraction(inputs[2], inputs[3])
    f2.num = inputs[2]
    f2.den = inputs[3]

    fractions_product = f1.product(f1,f2)
    print(f"The product of the two fractions is {fractions_product}")

if __name__ == '__main__': 
    start() # calling the start function