Number = int(input("Enter Number for Multiplication Table\n"))
Limit = int(input("Till How much you want\n"))
count = 1
print('Here is Your Multiplication  Table \n')
while count<=Limit:
       r = Number*count
       count = count+1 
       print( Number,'*', count-1 ,'=',r)