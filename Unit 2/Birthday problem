# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - calculate the probability that at least two people share a birthday in a class of 38 people
# Date - Monday September 26

number_of_students = 38 # the number of students in the class
no_matching = 1 

for n in range(number_of_students): # this for loop runs 38 times
  no_matching = no_matching * ((365-n)/365) # finding the probability of 2 students not having the same birthday
  
percentage = round(100* no_matching, 2) # change to a percentage
final_percentage = 100 - percentage # this line calculates the probability of 2 students having the same birthday
print(f"The chance of two people having the same birthday in a class of {number_of_students} people is {final_percentage}%") # print the output

# In this room of _38_ people, the probability of at least two people sharing the same birthday is: _86.41_% For a 50% probability, the minimum number of people needed is: _23_.
