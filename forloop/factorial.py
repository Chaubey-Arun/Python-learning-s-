n= int(input("Enter the Number - "))
fact = 1
count = 1
for count in range(1,n+1):
    fact = fact * count
    
print("factorial of a",n,"=",fact)
