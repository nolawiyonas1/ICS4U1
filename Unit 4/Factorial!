# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program will ask the user for an integer,calculate, then display the factorial
# Date - Friday November 11

def factorial(n): # this function calculates the factorial of a number 
  factorial_of_num = 1 # declaring the factorial variable
  for i in range(1,n + 1): # this for loop calculates the product of all positive integers from the selected number down to 1
    factorial_of_num = factorial_of_num * i 

  return factorial_of_num # return the calculated factorial number to the program

def get_n(): # this function asks the user for the value of n
  while True: # infinite while loop until the user enters a valid number
    try: # ensuring the user enters an integer
      num = int(input("Enter a number: ")) # asking the user for an input
      while True: # infinite while loop until the user enters a number greater than 0
        if num > 0:
          return num # return the number to the main program if it is greater than 0
        else:
          print("Please enter a number greater than 0.")
          num = int(input("Enter a num: ")) # asking the user for an input again until they enter a number greater than 0
    except: 
      print("Please enter an integer.") # print this text if the user does not enter an integer

def output(): # this function outputs the factorial for the user's number
  num = get_n() # calling the get_n() function
  factorial_answer = factorial(num) # calculate the factorial of "num"

  print(f"The factorial of {num} is {factorial_answer}") # printing the factorial
      
def start(): # start funciton that loops until the user indicates that they are done
  choice = input("Do you want to start?(y,n) ")
  while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # infinite loop if the user does not enter "y","Y","n" or "N"
    choice = input("Please enter 'y' or 'n': ") # telling the user to enter "y" or "n"

  while choice == 'y' or choice == 'Y': # while loop if the user enters "y"
    output() # call the output function if the user wants to start
    print("")
    choice = input('Do you want to run the program again? (y,n): ') # asking if the user wants to run the program again
    while choice != 'y' and choice != 'Y' and choice != "n" and choice != "N": # ensuring the user enters a proper input
      choice = input("Please enter 'y' or 'n': ") 

  if choice == 'n' or choice == "N":
    print("Thank you for using my program.") # print this if the user does not want to continue using the program

if __name__ == '__main__': 
  start() # calling the start function
