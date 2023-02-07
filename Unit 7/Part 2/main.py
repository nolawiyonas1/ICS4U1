# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - Using the text file 'qbdata.txt', this program has five functions: prints the first name, lastname, and passer rating to construct a simple sentence, prints the lastname followed by a comma and then the first name, prints the first and last name of the highest rated player, prints the average number of yards per completed pass and print out the last name, first name and then calculation, prints out the total number of players that completed over 300 passes
# Date - Monday January 26

def option_a(): # this function prints the first name, lastname, and passer rating to construct a simple sentence
  infile = open("qbdata.txt",'r') # opening the file
  for i in range(34): # looping 34 times (number of players)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    print(f"{words[0]} {words[1]} has a rating of {words[10]}") # displaying the sentence

  
def option_b(): # this function prints the lastname followed by a comma and then the first name
  infile = open("qbdata.txt",'r') # opening the file
  print("Last name, First name:") # displaying the format
  print()
  for i in range(34): # looping 34 times (number of players)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    print(f"{words[1]}, {words[0]}") # printing the lastname followed by a comma and then the first name


def option_c(): # this function prints the first and last name of the highest rated player
  infile = open("qbdata.txt",'r') # opening the file
  highest_rated_player = 0 # declaring a variable
  for i in range(34): # looping 34 times (number of players)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    if float(words[10]) > highest_rated_player: # checking if the rating is greater than the variable 'highest_rated_player'
      highest_rated_player = float(words[10]) # if it is greater, replace the variable
      first_name = words[0] # declaring the first name
      last_name = words[1] # declaring the last name
  print(f"The highest rated player is {first_name} {last_name} with a rating of {highest_rated_player}") # displaying the highest rated player along with their rating


def option_d(): # this function prints the average number of yards per completed pass 
  infile = open("qbdata.txt",'r') # opening the file
  for i in range(34): # looping 34 times (number of players)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    first_name = words[0] # declaring the first name
    last_name = words[1] # declaring the last name
    print(f"{last_name}, {first_name} has an average of {round(float(words[6]) / float(words[4]),2)} yards per completed pass.") # printing the average number of yards per completed pass 


def option_e(): # this function  prints out the total number of players that completed over 300 passes
  infile = open("qbdata.txt",'r') # opening the file
  number_of_players = 0 # declaring a variable that serves as a counter
  players = [] # opening a list to display the names
  for i in range(34): # looping 34 times (number of players)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    if int(words[4]) >= 300: # checking if the number of completed passes is over 300
      number_of_players += 1 # adding to the counter
      players += [f"{words[0]} {words[1]}"] # adding the player's name to the list
      
  print(f"The total number of players that completed over 300 passes is {number_of_players}.") # printing the total number of players that completed over 300 passes

  print("These players are:") # displaying their names
  print()
  for i in range(len(players)): # loop according to the number of players
    print(f"{players[i]}")


def user_input(): # this function asks for the user input
  print()
  print("Welcome to my program!") # displaying the choices
  print("A: Display the first name, last name, and passer rating of each player")
  print("B: Display the last name and first name of each player")
  print("C: Display the first and last name of the highest rated player")
  print("D: Display the average number of yards per completed pass for each player")
  print("E: Display the total number of players that completed over 300 passes")
  print()
  user_option = input("Enter you choice (a,b,c,d,e): ") # asking for the user's choice
  while user_option != "a" and user_option != "A" and user_option != "b" and user_option != "B" and user_option != "c" and user_option != "C" and user_option != "d" and user_option != "D" and user_option != "e" and user_option != "E": # ensuring the user enters a valid choice
    print()
    user_option = input("Please enter 'a', 'b', 'c', 'd' or 'e': ")
  print()
  if user_option == "a" or user_option == "A":
    option_a() # calling the option_a function
  if user_option == "b" or user_option == "B":
    option_b() # calling the option_b function
  if user_option == "c" or user_option == "C":
    option_c() # calling the option_c function
  if user_option == "d" or user_option == "D":
    option_d() # calling the option_d function
  if user_option == "e" or user_option == "E":
    option_e() # calling the option_e function


def main(): # this function asks the user if they want to start
  choice = input("Do you want to start? (y/n) ") # asking the user if they want to start
  
  while choice != "y" and choice != "yes" and choice != "n" and choice != "no": # keep looping until the user enters 'y','yes', 'n' or 'no'
    print()
    choice = input("Please enter 'y' or 'n': ")
  
  while choice == "y" or choice == "yes":
    user_input() # call the user_input function if the user enters 'y' or 'yes'
    print()
    choice = input("Do you want to run the program again?(y/n) ") # asking the user if they want to start again
    while choice != "y" and choice != "yes" and choice != "n" and choice != "no": # keep looping until the user enters 'y','yes', 'n' or 'no'
      print()
      choice = input("Please enter 'y' or 'n': ")

  while choice == "n" or choice == "no":
    print("Thank you for using my program") # print this if the user enters 'n' or 'no'
    break


if __name__ == "__main__":
    main() # calling the main function
