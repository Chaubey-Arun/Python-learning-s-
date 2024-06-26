l = [[1,2,3],[4,5,6],[7,8,9]]
m = [[9,8,7],[6,5,4],[3,2,1]]
c =[]

for i in range(len(l)):
    s=[]
    for j in range (len(l[0])):  
      s.append( l[i][j] + m[i][j] )               
    c.append((s))

print(c)
