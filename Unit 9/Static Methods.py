# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program returns the product of two fractions, returns the absolute value of a fraction, and checks if a fraction is positive
# Date - Friday March 03

import math # importing the math module to use its functions

class Fraction: # creating the class "Fraction"
    def __init__(self, n, d): # creating __init__ to initialize the attributes of an object
        # assigning the values to n and d
        self.num = n
        self.den = d
    
    @staticmethod # function decorator
    def product(f1_num, f1_den, f2_num,f2_den): # this method returns the product of two fractions
      gcd = math.gcd(int(f1_num*f2_num), int(f1_den*f2_den)) # calculating greatest common factor to display the fraction in the lowest terms
      numerator = int(f1_num*f2_num/gcd) # calculating the numerator
      denominator = int(f1_den*f2_den/gcd) # calculating the denominator      
      return (f"{numerator}/{denominator}") # returning the fraction to the main program
      
    @staticmethod # function decorator
    def absolute(f1_num, f1_den): # this method returns the absolute value of a fraction     
        numerator = abs(f1_num) # calculating the absolute value of the numerator
        denominator = abs(f1_den) # calculating the absolute value of the denominator        
        return (f"{int(numerator)}/{int(denominator)}") # returning the fraction to the main program
    
    @staticmethod # function decorator
    def is_positive(f1_num): # this method checks if a fraction is positive  
        if f1_num > 0: # return True if the numerator is greater than 0
            return True
        else: # return False otherwise
            return False

def user_input_2_fractions(): # this function asks the user for a numerator and denominator of two fractions
    while True: # infinte loop
        try: # ensuring that the user inputs an integer
            f1_num = float(input("Enter the numerator for f1: ")) # asking for the numerator of f1
            f1_den = float(input("Enter the denominator for f1: ")) # asking for the denominator of f1 
            f2_num = float(input("Enter the numerator for f2: ")) # asking for the numerator of f2
            f2_den = float(input("Enter the denominator for f2: ")) # asking for the denominator of f2 
            if f1_den != 0 or f2_den != 0: # ensuring that the denominators are not 0
                return f1_num, f1_den, f2_num, f2_den # return the values to the main program
            else: 
                print("Please enter a proper denominator (not equal to 0)")
        except:
            print("Please enter an integer")

def user_input_1_fraction(): # this function asks the user for a numerator and denominator of one fraction
    while True: # infinte loop
        try: # ensuring that the user inputs an integer
            f1_num = float(input("Enter the numerator for the fraction: ")) # asking for the numerator of f1
            f1_den = float(input("Enter the denominator for the fraction: ")) # asking for the denominator of f1  
            if f1_den != 0: # ensuring that the denominator is not 0
                return f1_num, f1_den # return the values to the main program
            else: 
                print("Please enter a proper denominator (not equal to 0)")
        except:
            print("Please enter an integer")

def choices(): # this function asks the user for the choices
    print() # displaying the choices
    print("A: Return the product of two fractions")
    print("B: Return the absolute value of a fraction")
    print("C: Check if a fraction is positive")
    print()
    choice = input("Enter your choice (A, B, C): ") # asking for the user's choices

    while choice != 'A' and choice != 'B' and choice != "C" and choice != "a" and choice != "b" and choice != "c": # ensuring the user enters a proper input
      choice = input("Please enter 'A', 'B' or 'C': ") 
      
    else:
        if choice == "A" or choice == "a": # if the user enters "A"
            inputs = user_input_2_fractions() # calling the 'user_input_2_fractions()' function
            fractions_product = Fraction.product(inputs[0], inputs[1], inputs[2], inputs[3]) # calling the 'products()' method 
            print(f"The product of the two fractions is {fractions_product}") # displaying the result
            print()

        if choice == "B" or choice == "b": # if the user enters "B"
            inputs_2 = user_input_1_fraction() # calling the 'user_input_1_fractions()' function
            fraction_absolute = Fraction.absolute(inputs_2[0], inputs_2[1]) # calling the 'absolute()' method 
            print(f"The absolute value of the fraction is {fraction_absolute}") # displaying the result
            print()

        if choice == "C" or choice == "c": # if the user enters "C"
            inputs_3 = user_input_1_fraction()  # calling the 'user_input_1_fractions()' function
            fraction_is_positive = Fraction.is_positive(inputs_3[0]) # calling the 'is_positive()' method 
            if fraction_is_positive == True: # if the fraction is positive
                print("True: The fraction is positive") # displaying the result

            elif fraction_is_positive == False: # if the fraction is not positive
                print("False: The fraction is not positive") # displaying the result
            print()
    
def start(): # this  funciton will loop until the user indicates that they are done using the program
  choice = input("Do you want to start? (y,n) ") # asking the user to start
  while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # ensuring the user enters a proper input
    choice = input("Please enter 'y' or 'n': ") 

  while choice == 'y' or choice == 'Y': 
    choices() # calling the choices function if the user wants to start
    choice = input('Do you want to run the program again? (y,n): ') # asking the user if they want to start again
    while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # ensuring the user enters a proper input
      choice = input("Please enter 'y' or 'n': ") 

  if choice == 'n' or choice == "N":
    print("Thank you for using my program.") # print this if the user does not want to run the program 

if __name__ == '__main__': 
    start() # calling the start function