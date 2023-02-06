# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program will display all of the prime numbers between 1 and the user's inputted number
# Date - Saturday October 15

def welcome(): # this function welcomes the user
  print("Welcome to the prime number program!")
  print("")

def is_prime(i):
  for divisor in range (2, i): # divosors are all the numbers between 2 and the user's inputted number
    if (i % divisor) == 0: # checking if the numbers are divisible 
      return True # return true if the number is not a prime
  return False # return False if the number is a prime

def check_prime_num(): # this function checks and displays all of the prime numbers between 1 and the user's inputted number
  welcome() # calling the welcome() function
  start = input("Do you want to start?(y/n): ").lower() # asking if the user wants to start
  
  while start == "y" or start == "yes": # infinite loop
  
    if start == "yes" or "y": 
      try: # checking that user's input is an integer
        num = int(input("Enter a number: ")) # asking user for a number
        print(f"The prime numbers between 1 and {num} are:") 
        
        for i in range(1, num+1): # all the numbers between 1 and the user's inputted number
          if i > 1: # every prime number is greater than 1
            if is_prime(i): 
              continue # continue if the number is prime
             # if the number is divisible by any number besides 1, it is not a prime number, therefore break
            else:
              print(i) # if the number is not divisible by any number other than 1, it is a prime number, therefore print the number
    
        print("")
        start = input("Do you want to start over?(y/n) ").lower() # asking the user if they want to start over
  
      except:
        print("Please enter an integer.") # print if the user does not input an integer
  
  print("Thank you for using this program!")

def main(): # this function calls the check_prime_num() function
  check_prime_num()

if __name__ == '__main__': 
  main() # calling the main function
