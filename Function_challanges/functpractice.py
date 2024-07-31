# def dicm(c,b=[]):
#     print(b)
#     b.append(c)
#     return b

# print(dicm(2))

# print(dicm(3))



# def add(a,b,c,/,d,e,*,f,g):
#     m= a+b+c+d+e+f+gr
#     return  m

# j= add(3,4,5,5,5,g=5,f=6)
# print(j)


# def acepted(*lelebhai,optionali = 0 ):
#     print(lelebhai,optionali)

# acepted((2,4,4,5,5,3),3)

# def run(a,b=0):
#     print(a,',',b)

# run((3,4,4))

# def run(a,b,c): 
#     print(a,b,c)

# l1= [1,3,4]
# l2 = 'kar'

# run(l1[0],l1[1],l1[2])

# # run(*l2)
# m = [1,2,3]
# k = iter(m)
# print(next(k))
# print(next (k))
# print(next(k))
# # print(next(k))

# def fun():
#     l= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
#     i =0
#     while True:
#         max = l[i]
#         i +=1
#         i = i % 7 
#         yield max
        


# m = fun()
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))


# def krotry(a,b,*,c,d): 
#     print(a,b,c,d)
#     return

# krotry((4,6),4,c=5,d=3)

# l=[23,3,3,3,4,3,3]
# # Here multivariable * is use to accept the  values from formal parameters 
# def revision(*excpt):  
#     print(type(excpt),excpt)
# #This is the where mutiple variable * was take in both formal and actual parameters 
# def multivariable(*excpt):
#     print(type(excpt),excpt)

# multivariable(*l)
# revision(3,3,44,3,3,4,3,34,3)

# #output (multivarable) = <class 'tuple'> (23, 3, 3, 3, 4, 3, 3)
# # output revision = <class 'tuple'> (3, 3, 44, 3, 3, 4, 3, 34, 3)


# m = [1,5,3]
# def var( *a):
#     for i in a:
#         print(i)

# var(*m)


# # Now this is for keyword Argument as it will return Dict

# def myfun(**vari):
#     print(vari)
#     return

# myfun(Maths =100,Physics=95 , Hindi=100 )   

# """ learnt form mistake that durring assignment 
# actual parameter will can pass string without any ' '    
#  """
# # output = {'Maths': 100, 'Physics': 95, 'Hindi': 100}

# G = 10 

# def FUNc():
#     global G
#     G =G +10 
#     a = 23
#     print('fun Global',G)
#     print('local variable ', locals())
#     return a 

# print('out global 2 ',G)
# a =FUNc()
# print('after fun declare ',G)

# print(a)
# # print('Global variables ' ,globals())












