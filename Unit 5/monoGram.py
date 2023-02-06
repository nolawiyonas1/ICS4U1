# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program asks the user for their name, then displays their monogram 
# Date - Monday December 5

def start(): # this function gives introduces the program and instructs the user on how to end the program
  print("Welcome to the monogram program!")
  print("If you want to end the program, enter a blank name.")
  main() # calling the main function

def monogram(name):
  user_name = name.split() # splitting the user's input
    
  first_name = user_name[0] # the first value in the list "name"
  lowercase_first_name = [x.lower() for x in first_name] # convert first name to lower case
          
  middle_name = user_name[1] # the second value in the list "name"
  lowercase_middle_name = [x.lower() for x in middle_name] # convert middle name to lower case
          
  last_name = user_name[2] # the third value in the list "name"
  uppercase_last_name = [y.upper() for y in last_name] # convert last name to upper case
      
  monogram = [] # create a list called monogram
        
  monogram.append(lowercase_first_name[0]) # add first name to the list "monogram"
  monogram.append(uppercase_last_name[0]) # add last name to the list "monogram"
  monogram.append(lowercase_middle_name[0]) # add middle name to the list "monogram"

  return monogram # returning monogram to the main program

def main(): # when this function is called, it asks the user for their name, then displays their monogram 
  while True: # infinite loop
    try: # execute code if no error occurs
      print()
      prompt = input("Enter your full name (first, middle, last): ") # asking the user for their name
  
      if prompt == "": # if a blank name is entered, end the program
        break
      else:
        user_monogram = monogram(prompt) # calling the 'monogram' function to create the monogram, then storing the value in the 'user_monogram' variable
        print()
        print("Monogram:") # printing the monogram
          
        print("-"*(len(user_monogram)+2)) # making a box around the monogram
        print(" ", *user_monogram, sep = "") # removing the brackets and quotations from the list "monogram"
        print("-"*(len(user_monogram)+2))
        print()
    except: # execute this code if the user does not enter a valid input
      print("Enter your full name!")

  print("")
  print("Thank you for using my program!") # print this if the user is finished with the program

if __name__ == '__main__': 
  start() # calling the start function
