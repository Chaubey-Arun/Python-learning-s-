No_Number= int(input("Enter No of Number of number's "))
max =int(input("Enter Number"))
count=0
while No_Number-1 >count:
    n=int(input("Enter Number"))
    if n>max:
        max=n
    count+=1
print("maximum number", max)
