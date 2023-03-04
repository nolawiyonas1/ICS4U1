#### INCOMPLETE ####

import math

class Fraction:
    def __init__(self, n, d): 
        self.num = n
        self.den = d
    
    @staticmethod # function decorator
    def product(f1_num, f1_den, f2_num,f2_den):    
      gcd = math.gcd(int(f1_num*f2_num), int(f1_den*f2_den))      
      numerator = int(f1_num*f2_num/gcd)      
      denominator = int(f1_den*f2_den/gcd)       
      return (f"{numerator}/{denominator}") 
      
    @staticmethod # function decorator
    def absolute(f1_num, f1_den):      
        numerator = abs(f1_num)      
        denominator = abs(f1_den)        
        return (f"{int(numerator)}/{int(denominator)}")
    
    @staticmethod # function decorator
    def is_positive(f1_num):
        if f1_num > 0:
            return True
        else:
            return False

def user_input_2_fractions(): 
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

def user_input_1_fraction(): 
    while True:
        try: 
            f1_num = float(input("Enter the numerator for the fraction: ")) 
            f1_den = float(input("Enter the denominator for the fraction: ")) 
            if f1_den != 0: 
                return f1_num, f1_den
            else: 
                print("Please enter a proper denominator (not equal to 0)")
        except:
            print("Please enter an integer")

def start():
    inputs = user_input_2_fractions()
    fractions_product = Fraction.product(inputs[0], inputs[1], inputs[2], inputs[3])  
    print(f"The product of the two fractions is {fractions_product}")

    inputs_2 = user_input_1_fraction()
    fraction_absolute = Fraction.absolute(inputs_2[0], inputs_2[1])
    print(f"The absolute value of the fraction is {fraction_absolute}")

    inputs_3 = user_input_1_fraction()
    fraction_is_positive = Fraction.is_positive(inputs_3[0])
    if fraction_is_positive == True:
      print("True: The fraction is positive")

    elif fraction_is_positive == False:
      print("False: The fraction is negative")
    

if __name__ == '__main__': 
    start() # calling the start function
