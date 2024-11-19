'''map my work:
- user input for floats a b c
- calculate root and use quad form (math module)
- return x values'''

# enter math module 
import math 

#get input values
a = int(input("Enter 'a' value:"))
b = int(input("Enter 'b' value:"))
c = int(input("Enter 'c' value:"))

#calculate quadratic formula with both neg and pos
results = (-b + math.sqrt(b **2 - 4 * a * c)) / (2 * a)
results2 = (-b - math.sqrt(b **2 - 4 * a * c)) / (2 * a)

#print results 
print("X=", results, "and X=", results2)