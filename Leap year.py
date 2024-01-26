year = int(input("Enter Year"))
if year%100==0:
    if year%400==0:
        print("Leap Year")
    else:
        print("Its not a leap year")
