# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program include everything from the "Instance Methods" program, and an __init__ method that ensures that the radius is positive
# Date - Wednesday February 15

import math # importing the math module to use its functions

class Circle: # creating the class "Circle"

  def __init__(self, x, y, r): # this method ensures that the radius is positive
    if r < 0: # if radius is negative
      r = -r # Converting r to a positive value

    # assigning the values to the circle class
    self.__x = x
    self.__y = y
    self.__r = r

  def area_of_circle(self): # this method returns the area of a circle
    area = math.pi * self.r**2 # calculating the area
    return area # returning area to the main program
      
  def smaller(self,c2): # this method returns the smaller circle
    area_of_c1 = math.pi * self.r**2 # calculating the area of the first circle 
    area_of_c2 = math.pi * c2.r**2 # calculating the area of the second circle 
      
    if area_of_c1 <= area_of_c2: # if the first circle is smaller or equal to the second circle, return it
      area_word1 = "Circle 1"
      return area_word1, area_of_c1 # return to the main program
    else: # if the second circle is smaller than the first circle, return it
      area_word2 = "Circle 2"
      return area_word2, area_of_c2 # return to the main program

def get_input(): # this function asks for the user input
  while True: # infinite loop
    try: # ensuring that the user inputs a float
      x = float(input("Enter the x coordinate: ")) # asking for the x coordinate
      y = float(input("Enter the y coordinate: ")) # asking for the y coordinate
      r = float(input("Enter the radius: ")) # asking for the radius
      if r != 0: # ensuring that the radius is not 0
          return x,y,r # return to the main program
      else: 
          print("Please enter a proper radius (not equal to 0)")
    except:
      print("Please enter a float")

def start(): # this function calls the functions/classes above to perform tasks
  print("Circle 1")
  inputs_1 = get_input() # asking for the first user inputs

  c1 = Circle(inputs_1[0], inputs_1[1], inputs_1[2]) # creating a c1 object
  c1.x = inputs_1[0] # first number of the user's input is the x coordinate
  c1.y = inputs_1[1] # second number of the user's input is the y coordinate
  c1.r = inputs_1[2] # third number of the user's input is the radius
  area_of_circle1 = round(c1.area_of_circle(), 2) # calculating the area of the circle
  print(f"The area of the circle 1 is {area_of_circle1}") # displaying the area
  print()

  print("Circle 2")
  inputs_2 = get_input()

  c2 = Circle(inputs_2[0], inputs_2[1], inputs_2[2]) # creating a c2 object
  c2.x = inputs_2[0] # first number of the user's input is the x coordinate
  c2.y = inputs_2[1] # second number of the user's input is the y coordinate
  c2.r = inputs_2[2] # third number of the user's input is the radius
  area_of_circle2 = round(c2.area_of_circle(), 2) # calculating the area of the circle
  print(f"The area of the circle 2 is {area_of_circle2}") # displaying the area
  print()

  c3 = c1.smaller(c2) # calling smaller() to determine the smaller circle
  print(f"The smaller circle is {c3[0]} with an area of {round(c3[1], 2)}") # displaying the smaller circle
  print()

if __name__ == '__main__': 
  start() # calling the start function
