

for n in range (1,10000):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
         count+=1
    if count==2:
       print( i,end=' ') 
