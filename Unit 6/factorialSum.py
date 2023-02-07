# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program calculates the sum of all factorials of the numbers entered by the user. 
# Date - 01/15/23


def factorial(): # this function calculates the factorial of multiple numbers, and ensures that these numbers are integers greater than 0
  num = 1 # declaring the 'num' variable
  sum = 0 # declaring the 'sum' variable
  while num != 0: # this will loop continuously until the enters '0'
    try: # ensuring the the user enters an integer
      num = int(input("Enter a number (Enter 0 when finished): ")) # asking the user for a number to calculate the factorial

      if num >= 0: # ensuring that the user enters a number greater than 0
        factorial_of_num = 1 # declaring a variable
        for i in range(1,num + 1): # this for loop acts like a formula to calculate the factorials
          factorial_of_num = factorial_of_num * i 
        
        sum += factorial_of_num # adding the new factorial to the variable 'factorial_of_num'

      else:
        print("Please enter an integer greater than 0.") # telling the user to enter an integer greater than 0
        print()
      
    except:
      print("Please enter an integer.") # telling the user to enter an integer 
      print()

  else:
    return sum-1 # return the sum to the main program
    

def output(): # this function displays the results to the user
  final_answer = factorial() # calling the factorial function to calculate the factorial

  print(f"The sum of all factorials is {final_answer}") # printing the sum of all factorials

      
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
