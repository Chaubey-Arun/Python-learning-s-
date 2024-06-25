# l1 = [x for x in range(10) ]
# l2= [x*2 for x in range (2,7)]
# l3 =[x for x in 'arunkumar23@gmail.com' if x.isalpha()]
# l4 = [x.lower() for x in 'PYTHON']
# print(l1,l2,l3,l4)
# n = 0
# while 1>n :
#     num = list(input('Enter a Number to check whether it is palindorm or not '))
#     rev=[]
#     for i in range (-1,-(len(num) +1),-1):
#         rev.append(num[i])
#     if rev == num:
#         print('its a Palindrone ')
#         n = n+1    
#     else :
#         print('Re-Enter ')


for _ in range(1):
    num = input('Enter a Number to check whether it is a palindrome or not: ')
    rev = num[::-1]
    if rev == num:
        print('It is a Palindrome!')
        break
    else:
        print('Not a Palindrome. Re-enter!')

# rev = num[ : :-1]
# print(rev)
# rev = [ ]
# sep=''
# for i in range (-1,-(len(num) +1),-1):
#       rev.extend(num[i])
# print (rev)
# l1 = sep.join(rev)
# print(l1)
# if rev==l1 :
#        print ('it is pallindrom ')
# else:
#        print('Re-Enter the value ')

1#convert a given string to palindrome 
# str1= input('Enter to check Palindrome -')
# n=len(str1)
# str2 = str1[-1:-(len(str1) +1):-1]

# print(str2)
# str4 = str3[::-1]
# if (str4 == str3):
#     print('Palindrome')
# else:
#     print('it is not ')

