s1 = input('Enter the string')
lower = ''
upper = ''
for i in s1:
    if  i.islower():
        lower= lower + i 
    elif i.isupper():
        upper= upper+i 

str2= upper +lower

print('The upper lower rearangig  ',str2)
      
