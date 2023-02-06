# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program asks the user for an integer, then determines if it is exceptional or not based on a calculated exceptioon and standard deviation 
# Date - Friday December 9

import random # importing the random module to use its functions

def exceptional_checker(user_integer, exception, final_standard_deviation): # this function checks if the user's integer is exceptional or not
  if user_integer < (exception - final_standard_deviation) or user_integer > (exception + final_standard_deviation): # formula to determine if the user's integer is exceptional or not
    print(f"{user_integer} is an exception of {exception} with a standard deviation of {final_standard_deviation}") # print this if the user's integer is exceptional
    print()
  else:
    print(f"{user_integer} is not an exception of {exception} with a standard deviation of {final_standard_deviation}") # print this if the user's integer is not exceptional
    print()

def calculate_standard_deviation(): # This function calculates, then returns exception and standard deviation
  ### FIRST LIST
  integers = [] # creating a list to store 150 integers
  sum = 0 # the sum of the integers
  
  for i in range(150): # looping to generate 150 numbers
    random_num = random.randint(25,75) # generating numbers between 25 and 75
    integers.append(random_num) # adding the generated numbers into the list 'integers'
    sum += random_num # add the value of the generated number to the variable 'sum'
  
  ### First average
  u = round(sum/150, 2) # finding the average of the 150 generated numbers
  
  ### SECOND LIST
  squared_error = [] # creating a list to store the square of differences
  sum_2 = 0 # the sum of the values in the list 'squared_error'
  
  for i in range(150): # looping 150 times
    square_of_differences = (integers[i] - u)**2 # finding the squared error between the data points and the average
    squared_error.append(square_of_differences) # adding the values to the list 'squared_error'
    sum_2 += square_of_differences # add the value of the square of differences to the variable 'sum_2'
  
  ### Second average
  v = round(sum_2/150, 2) # finding the average of the new list
  
  ### STANDARD DEVIATION
  standard_deviation = round(v**0.5, 2) # standard deviation is the square root of v

  return u, standard_deviation # returning u and standard_deviation to the main program

def user_input(): # this function asks for the user input
  while True: # infinite loop
    try: # ensuring the user enters an integer
      user_integer = int(input("Enter an integer: ")) # asking the user for an integer
      exception, final_standard_deviation = calculate_standard_deviation() # getting the exception and standard deviation
      exceptional_checker(user_integer, exception, final_standard_deviation) # calling the exceptional_checker function to check if the user's integer is exceptional or not
      break # break to ask the user if they want to restart the program
    except:
      print("Please enter an integer!")

def main(): # this function asks the user if they want to start
  choice = input("Do you want to start?(y/n) ") # asking the user if they want to start
  
  while choice != "y" and choice != "yes" and choice != "n" and choice != "no": # keep looping until the user enters 'y','yes', 'n' or 'no'
    print()
    choice = input("Please enter 'y' or 'n': ")
  
  while choice == "y" or choice == "yes":
    user_input() # call the user_input function if the user enters 'y' or 'yes'
    choice = input("Do you want to start again?(y/n) ") # asking the user if they want to start again
    while choice != "y" and choice != "yes" and choice != "n" and choice != "no": # keep looping until the user enters 'y','yes', 'n' or 'no'
      print()
      choice = input("Please enter 'y' or 'n': ")

  while choice == "n" or choice == "no":
    print("Thank you for using my program") # print this if the user enters 'n' or 'no'
    break

if __name__ == "__main__":
  main() # calling the main function
