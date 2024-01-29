n= int(input("Enter No of Number of number's "))
binary =0 
sum = 0 
while n>0:
    r = n%2 
    n=n//2
    sum= sum*10 + r 

while sum>0:
     d = sum%10
     sum=sum //10
    
     binary= binary*10 + d

print("Binary Number is ",binary)


