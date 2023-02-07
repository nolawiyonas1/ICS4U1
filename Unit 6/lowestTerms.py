# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program takes a positive fraction and returns it in lowest terms
# Date - 01/20/23


def greatest_common_divisor(n, d): # this function serves as a greatest common divisor algorithm
  while d: # Euclidean algorithm
      n, d = d, n % d 
  return n # returning n to the main program


def simplify_fraction(): # this function does the input checks and returns the lowest term to the main program
  while True: # infinte loop
    try: # ensuring the user enters a valid input
      user_fraction = input("Enter a fraction in the form of 'n/d': ") # asking for the user input

      if user_fraction.count("/") > 1: # ensuring that the user enters '/' only once
        print("Please enter only one '/'")
        print()

      else: # execute this code if the user enters only one '/'
        new_fraction = user_fraction.split("/") # splitting the string
        numerator = int(new_fraction[0]) # defining the numerator
        denominator = int(new_fraction[1]) # defining the denominator
  
        if numerator > 0 and denominator > 0: # ensuring that the fraction is positive
          gcd_value = greatest_common_divisor(numerator, denominator) # calling the 'greatest_common_divisor function'

          lowest_term = f'{numerator//gcd_value}/{denominator//gcd_value}'
          
          return lowest_term # returning the lowest term to the main program
        
        else:
          print("Please enter a positive fraction.") # telling the user to enter a positive fraction
          print()
      
    except:
      print("Please enter a fraction in the form of 'n/d'") # telling the user to enter a fraction in the form of 'n/d'
      print()
      

def output(): # this function displays the results to the user
  final_fraction = simplify_fraction() # calling the simplify_fraction function to calculate the lowest term
  
  print(f"The fraction in the lowest terms is {final_fraction}") # printing the lowest term
  
      
def start(): # this  funciton will loop until the user indicates that they are done using the program
  choice = input("Do you want to start? (y,n) ") # asking the user to start
  while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # ensuring the user enters a proper input
    choice = input("Please enter 'y' or 'n': ") 

  while choice == 'y' or choice == 'Y': 
    output() # calling the output function if the user wants to start
    print("")
    choice = input('Do you want to run the program again? (y,n): ') # asking the user if they want to start again
    while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # ensuring the user enters a proper input
      choice = input("Please enter 'y' or 'n': ") 

  if choice == 'n' or choice == "N":
    print("Thank you for using my program.") # print this if the user does not want to run the program 


if __name__ == '__main__': 
  start() # calling the start function
