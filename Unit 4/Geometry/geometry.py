import math # import math to use its functions

def area_rectangle(length, width): # this function calculates the area of a rectangle
  area_of_rectangle = length * width # formula to find area of a rectangle
  return area_of_rectangle # returning the area to the main program

def area_circle(radius): # this function calculates the area of a circle
  area_of_circle = math.pi * (radius)**2 # formula to find area of a circle
  return area_of_circle # returning the area to the main program

def circumference(radius): # this function calculates the circumference of a circle
  circumference_of_circle = math.pi * (radius*2) # formula to find circumference of a circle
  return circumference_of_circle # returning the circumference to the main program

def volume_rectangular_prism(length, width, height): # this function calculates the volume of a rectangular prism
  volume_of_rectangular_prism = length * width * height # formula to find volume of a rectangular prism
  return volume_of_rectangular_prism # returning the volume to the main program

def volume_cylinder(radius, height): # this function calculates the volume of a cylinder
  volume_of_cylinder = math.pi * (radius**2) * height # formula to find volume of a cylinder
  return volume_of_cylinder

def surface_area_rectangular_prism(length, width, height): # this function calculates the surface area of a rectangular prism
  first_area = area_rectangle(width, length) # area of the first pair of rectangles on the prism
  second_area = area_rectangle(height, length) # area of the second pair of rectangles on the prism
  third_area = area_rectangle(height, width) # area of the third pair of rectangles on the prism
  surface_area_of_rectangular_prism = 2*(first_area+second_area+third_area) # formula for the surface area of a rectangular prism
  return surface_area_of_rectangular_prism # returning surface area to the main program

def surface_area_cylinder(radius, height): # this function calculates the surface area of a cylinder
  circumference_cylinder = circumference(radius) # the width of the middle part of the cylinder
  height_cylinder = height # the height of the middle part of the cylinder
  radius_cylinder = 2 * area_circle(radius) # the area of the top and bottom circles on the cylinder
  rectangle_cylinder = area_rectangle(height_cylinder, circumference_cylinder) # the area of the middle part of a cylinder
  surface_area_of_cylinder = rectangle_cylinder + radius_cylinder # calculating the surface area of they cylinder
  return surface_area_of_cylinder
