# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program calculates and displays the volume and surface area of a rectangular prism or 
# Date - Friday November 11

from geometry import * # importing the geometry.py file to use its functions

def get_length_rectangular_prism(): # this function gets the value of length from the user and uses it to calculate the volume and surface area of a rectangular prism
  while True: # infinite loop until the user enters a valid input
    try: # ensuring the user enters an integer
      length_of_prism = int(input("Enter length: ")) # asking for the user input
      return length_of_prism # return length to the main program
    except:
      print("Please enter an integer.")

def get_width_rectangular_prism(): # this function gets the value of width from the user and uses it to calculate the volume and surface area of a rectangular prism
  while True: # infinite loop until the user enters a valid input
    try: # ensuring the user enters an integer
      width_of_prism = int(input("Enter width: ")) # asking for the user input
      return width_of_prism # return width to the main program
    except:
      print("Please enter an integer.")

def get_height_rectangular_prism(): # this function gets the value of height from the user and uses it to calculate the volume and surface area of a rectangular prism
  while True: # infinite loop until the user enters a valid input
    try: # ensures the user enters an integer
      height_of_prism = int(input("Enter height: ")) # asking for the user input
      return height_of_prism # return height to the main program
    except:
      print("Please enter an integer.")


def get_radius_cylinder(): # this function gets the value of radius from the user and uses it to calculate the volume and surface area of a cylinder
  while True: # infinite loop until the user enters a valid input
    try: # ensures the user enters an integer
      radius_of_cylinder = int(input("Enter radius: ")) # asking for the user input
      return radius_of_cylinder # return radius to the main program
    except:
      print("Please enter an integer.") 

def get_height_cylinder(): # this function gets the value of height from the user and uses it to calculate the volume and surface area of a cylinder
  while True: # infinite loop until the user enters a valid input
    try: # ensures the user enters an integer
      height_of_cylinder = int(input("Enter height: ")) # asking for the user input
      return height_of_cylinder # return height to the main program
    except:
      print("Please enter an integer.") 

def calculate_rectangular_prism(): # this funciton calculates, then displays the volume and surface area of a rectangular prism
  final_length_of_prism = get_length_rectangular_prism() # calling the get_length_rectangular_prism function to get the value of length from the user
  final_width_of_prism = get_width_rectangular_prism() # calling the get_width_rectangular_prism function to get the value of width from the user
  final_height_of_prism = get_height_rectangular_prism() # calling the get_height_rectangular_prism function to get the value of height from the user
  print("")
  final_area1_rectangular_prism = round(area_rectangle(final_width_of_prism, final_height_of_prism), 2) # calculating area of the first pair of opposite faces on the rectangular prism
  final_area2_rectangular_prism = round(area_rectangle(final_width_of_prism, final_length_of_prism), 2) # calculating area of the second pair of opposite faces on the rectangular prism
  final_area3_rectangular_prism = round(area_rectangle(final_length_of_prism, final_height_of_prism), 2) # calculating area of the third pair of opposite faces on the rectangular prism
  print(f"The area of the first pairs of rectangles on the prism is {final_area1_rectangular_prism}") # printing the first area 
  print(f"The area of the second pairs of rectangles on the prism is {final_area2_rectangular_prism}") # printing the second area
  print(f"The area of the third pairs of rectangles on the prism is {final_area3_rectangular_prism}") # printing the third area
  print("")
  final_volume_rectangular_prism = round(volume_rectangular_prism(final_length_of_prism, final_width_of_prism, final_height_of_prism), 2) # calling the volume_rectangular_prism function from the geometry.py file to calculate the volume of a rectangular prism
  print(f"The volume of the rectangular prism is {final_volume_rectangular_prism}") # printing the volume
  final_surface_area_rectangular_prism = round(surface_area_rectangular_prism(final_length_of_prism, final_width_of_prism, final_height_of_prism), 2)  # calling the surface_area_rectangular_prism function from the geometry.py file to calculate the surface area of a rectangular prism
  print(f"The surface area of the rectangular prism is {final_surface_area_rectangular_prism}") # printing the surface area

def calculate_cylinder(): # this funciton calculates, then displays the volume and surface area of a cylinder
  final_radius_of_cylinder = get_radius_cylinder() # calling the get_radius_cylinder function to get the value of radius from the user
  final_height_of_cylinder = get_height_cylinder() # calling the get_height_cylinder function to get the value of height from the user
  print("")
  final_area_circle = round(area_circle(final_radius_of_cylinder), 2) # calculating the area of the circle
  print(f"The area of the circle is {final_area_circle}") # printing the area
  final_circumference_circle = round(circumference(final_radius_of_cylinder), 2) # calculating the circumference of the circle
  print(f"The circumference of the circle is {final_circumference_circle}") # printing the circumference
  print("")
  final_volume_cylinder = round(volume_cylinder(final_radius_of_cylinder, final_height_of_cylinder), 2) # calling the volume_cylinder function from the geometry.py file to calculate the volume of a cylinder
  print(f"The volume of the cylinder is {final_volume_cylinder}") # printing the volume
  final_surface_area_cylinder = round(surface_area_cylinder(final_radius_of_cylinder, final_height_of_cylinder), 2)  # calling the surface_area_cylinder function from the geometry.py file to calculate the surface area of a cylinder
  print(f"The surface area of the cylinder is {final_surface_area_cylinder}") # printing the surface area

def main_program(): # this function asks the user to select either a rectangular prism or a cylinder
  print("")
  print("1. Rectangular prism")
  print("2. Cylinder")
  print("")
  choice = input("What is your choice?(1,2) ") # asking for the user's choice
  print("")

  while choice != "1" and choice != "2": # ensures the user enters '1' or '2'
    choice = input("Please enter '1' or '2': ")
    print("")

  if choice == "1":
      calculate_rectangular_prism() # calculate the volume and surface area of a rectangular prism if the user chooses '1'
    
  if choice == "2":
      calculate_cylinder() # calculate the volume and surface area of a cylinder if the user chooses '2'

def start(): # this function asks the user if they want to start or end the program
  start_choice = input("Do you want to start?(y/n) ") # asking the user if they want to start
  
  while start_choice != 'y' and start_choice != 'Y' and start_choice != "n" and start_choice != "N": # infinite loop if the user does not enter "y","Y","n" or "N"
    start_choice = input("Please enter 'y' or 'n': ") # telling the user to enter "y" or "n"
  
  while start_choice == 'y' or start_choice == 'Y': # while loop if the user enters "y"
    main_program() # calling the main_program function so the user chooses between rectangular prism and cylinder
    print("")
    start_choice = input('Do you want to run the program again? (y,n): ') # asking if the user wants to run the program again
    while start_choice != 'y' and start_choice != 'Y' and start_choice != "n" and start_choice != "N": # infinite loop if the user does not enter "y","Y","n" or "N"
      start_choice = input("Please enter 'y' or 'n': ") # telling the user to enter "y" or "n"
    else:
      continue # continue normally if the user inputs 'y' or 'n'
  
  if start_choice == 'n' or start_choice == "N":
    print("Thank you for using my program.") # print this if the user does not want to continue using the program

if __name__ == '__main__': 
  start() # calling the start function
