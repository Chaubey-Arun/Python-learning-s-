# print 12345 
n= int(input('Enter Number to get sequence from the Right \n'))
while (n>0):
    r= (n%10)
    n= (n//10)
    print(r)
