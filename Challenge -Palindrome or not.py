n = int(input("Enter the number"))
d=n
count=0 
while n>0:
     r =n% 10 
     n  =n//10
     count = count*10 + r
print("Reverse Number",count)
if d==count:
     print("The Number is Palindorme")
else:
     print("It is not a palindrome")