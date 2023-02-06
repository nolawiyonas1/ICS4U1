# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program solves a quadratic formula, checks if the equation has zero, one, or two solutions, then display the result
# Date - Wednesday September 21, 2022

import math # importing math to use it's functions

# creating inputs for the a, b and c values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# formula for discriminant
discriminant = (b**2) - (4*a*c)

# if the discriminant is greater than 0, there will be two solutions 
if discriminant > 0:
  print("This equation has two solutions")
  solution = round(((-1*b)+math.sqrt(b**2-4*a*c))/(2*a),2)
  solution2 = round(((-1*b)-math.sqrt(b**2-4*a*c))/(2*a),2)
  print(solution) # print the solutions
  print(solution2) 

# if the discriminant is equal to 0, there will be one solution
elif discriminant == 0:
  print("This equation has one solution")
  solution = round(((-1*b)+math.sqrt(b**2-4*a*c))/(2*a),2)
  print(solution) # print the solution

# if the discriminant is less than 0, there will be no solutions
elif discriminant < 0: 
  print("This equation has no solution")
