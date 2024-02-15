# Display data in given format(25 letters )
 #product Name ....price
#chiken Pizza ........300
#we used length function to calcultate the length 
# we multiply '.' char with 25 - total length 
Name= input('Enter Product Name')
price=input('Enter Price of Product')
total =len( Name)+len(price) 
print(total)
dot = '.'*(25-total)
print(Name,dot,price)
