# Name - Nolawi Teklehaimanot
# Grade - 12
# Description - This program includes statements that perform specific tasks 
# Date - Wednesday February 15

'''
Assuming that two objects f1 and f2 of type Fraction have been created and assigned values, the statements below perform a specific task.

A) This statement doubles the value of f1
  f1.num *= 2

B) This statement inverts f2
  temp_num = f2.num # creating a temporary number to invert the fraction
  f2.num = f2.den
  f2.den = temp_num

C) This statement makes f1 equal to the (unsimplified) product of f1 and f2
  f1.num = f1.num * f2.num # multiplying the numerators
  f1.den = f1.den * f2.den # multiplying the denominators

D) This statement makes f2 equal to the (unsimplified) sum of f1 and f2
  f2.num = (f1.num*f2.den) + (f2.num *f1.den) # formula to add two fractions with different denominators
  f2.den = (f1.den*f2.den)

E) This statement makes f1 equal to ∣f1∣ (the absolute value of f1)
  f1.num = abs(f1.num) # absolute value of the numerator
  f1.den = abs(f1.den) # absolute value of the denominator

'''
