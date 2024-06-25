# # # l = [int(x) for x in input('Enter the working Days seprated by spaces ').split()]
# # # print(sum(l))


# # # # sum= 0

# # # # for i in range(len(l)):
# # # #   sum = sum + int(l[i])  #sum of day 

# # # # print(Price = sum * 70)
# # ---------------------------------------------------------------------------------------
# # # REMOVE DUBPLICATE 
# # # a = [1,3,34,55,3,5,6,5]
# # # m = []
# # # for x in a : 
# # #     if x not  in m :
#         m.append(x)

# # # print(m)

# ------------------------------------------------------
# CONCATENATE ALL INTERGER FROM A LIST TO A SINGLE NUMBER 
# THINK IN TERM'S OF STRING 
# A = [2,3,5,6]
# st = ''
# for x in A : 
#   st += str(x)

# print(int(st))

# ------------------------------------------------------------
# L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

# L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

# index1 = 10
# index2 = 10

# for x in L1:
#     z1 = L1.index(x)
#     z2 = L2.index(x)
#     m = z1+z2
#     if m < index1+index2:
#         index1 = z1
#         index2 = z2

# print(L1[index1],index1+index2)
# ---------------------------------------------------------
#overlapping number 
# L1 = [10, 15, 6, 9, 12, 8, 4]

# L2 = [14, 6, 19 , 4, 7, 10, 11]

# l3 = [  ]
 
# for i in L1:
#     if i in L2:
#         l3.append(i)

# print (l3)
# ---------------------------------------------------------------------
# Most Occurance 
# L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']

# result = []

# for i in L1:
#     if i not in result:
#         result.append(i)
#         x=L1.count(i)
#         result.append(x)

# print(result)
#-----------------------------------------------------------------------
# Morse.py

codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

Text = 'deface' 
m=' '
for i in Text:
     m += codes[ord(i) - 97]+ ' '
    
print(m)