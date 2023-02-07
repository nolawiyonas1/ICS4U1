# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - Using the text file 'studentdata.txt', this program has three functions: display the names of the students that have more than six quiz scores, display the average grades for each student, display the maximum and minimum scores for each student
# Date - Monday January 23

def option_a(): # this function displays the names of the students that have more than six quiz scores 
  print("The students that have more than six quiz scores are:")
  infile = open("studentdata.txt",'r') # opening the file
  for i in range(5): # looping 5 times (number of students)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    if len(words) > 7: # print the student's name if the line has more than 7 words
      print(words[0].title())


def option_b(): # this functino displays the average grades for each student
  print("The average grades for each student are:")
  infile = open("studentdata.txt",'r') # opening the file
  for i in range(5): # looping 5 times (number of students)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    sum = 0 # declaring the sum variable
    for i in range(1, len(words)): # loop through the code according to the number of words in the line (excluding the name)
      sum += int(words[i]) # adding the numbers
      average = round((sum)/(len(words)-1), 2) # diving the sum by the amount of numbers

    print(f"{words[0].title()}: {average}") # print the name and average of each student


def option_c(): # this function displays the maximum and minimum scores for each student
  print("The maximum and minimum scores for each student are (max,min):")
  infile = open("studentdata.txt",'r') # opening the file
  for i in range(5): # looping 5 times (number of students)
    data = infile.readline() # reading the line
    words = data.split() # splitting the line into words
    print(f"{words[0].title()}: {max(words[1:],key=int)}, {min(words[1:],key=int)}") # print the maximum and minimum scores of each student


def user_input(): # this function asks for the user input
  print()
  print("Welcome to my program!") # displaying the choices
  print("A: Display the name of the students with more than six quiz scores")
  print("B: Display the average of each student")
  print("C: Display the maxium and minimum score of each student")
  print()
  user_option = input("Enter you choice (a,b,c): ") # asking for the user's choice
  while user_option != "a" and user_option != "A" and user_option != "b" and user_option != "B" and user_option != "c" and user_option != "C": # ensuring the user enters a valid choice
    print()
    user_option = input("Please enter 'a', 'b' or 'c': ")
  print()
  if user_option == "a" or user_option == "A":
    option_a() # calling the option_a function
  if user_option == "b" or user_option == "B":
    option_b() # calling the option_b function
  if user_option == "c" or user_option == "C":
    option_c() # calling the option_c function


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
