import math 
print("Find Out the Root Of the Quaderatic Equation")
A = float(input("input coffeciant A"))
B = float(input("input Coffeciant B"))
C = float(input("input Constant C"))
Root_1 = (-B**2 - (math.sqrt(B**2-4*A*C)) ) / (2*A)
Root_2 = (-B**2 + (math.sqrt(B**2-4*A*C)) ) / (2*A)
print("Square roots are - ",Root_1,Root_2)