amount= float(input("Enter Amount\n"))
if amount<=1000:
    DisAmount=amount*(10/100)
    

elif amount>1000 and amount<=5000:
     DisAmount= amount*(20/100)
     
elif amount>5000 and amount<=10000:
     DisAmount= amount*(30/100)
    
else:
     DisAmount= amount*(50/100)

Final_Price = amount - DisAmount
print("Discount Price",DisAmount)
print("Final Price",Final_Price)