# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program will convert the inputted number to ascii, hexadecimal or binary, then print out the conversion
# Date - Friday October 14

# FUNCTIONS

def convert_to_ascii(): # this function converts a number to ascii
  ascii_input = int(input("Enter a number: ")) # asking for user input
  converted_ascii = chr(ascii_input) # converting the inputted number to ascii
  print(f"The converted number is {converted_ascii}") # print conversion
  print("")

def convert_to_hexadecimal(): # this function converts a number to hexadecimal
  hexadecimal_input = int(input("Enter a number: ")) # asking for user input
  converted_hexadecimal = hex(hexadecimal_input) # converting the inputted number to hexadecimal
  print(f"The converted number is {converted_hexadecimal}") # print conversion
  print("")

def convert_to_binary(): # this function converts a number to binary
  binary_input = int(input("Enter a number: ")) # asking for user input
  converted_binary = bin(binary_input) # converting the inputted number to binary
  print(f"The converted number is {converted_binary}") # print conversion
  print("")

def options(): # this function will print the 4 options
  
  print ("Welcome to the decimal conversion program!")
  
  print("1: Convert to ASCII")
  print("2: Convert to Hexadecimal")
  print("3: Convert to Binary")
  print("4: Exit")
  print("")
  
  choice = ""
  
  while choice != "4": # infinite loop
  
    choice = input("What is your choice?(1,2,3,4) ")
    
    if choice == "1":
      convert_to_ascii() # calling the function
    
    elif choice == "2":
      convert_to_hexadecimal() # calling the function
    
    elif choice == "3":
      convert_to_binary() # calling the function
  
  print("Thank you for using the decimal converter!")

def main(): # this function will call the options functions
  options()

if __name__ == '__main__': 
  main() # calling the main function
