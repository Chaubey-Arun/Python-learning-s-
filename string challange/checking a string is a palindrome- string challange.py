1#convert a given string to palindrome 
str1= input('Enter to check Palindrome -')
n=len(str1)
str2 = str1[::-1]
str3 = str2 + str1
print(str3)
str4 = str3[::-1]
if (str4 == str3):
    print('Palindrome')
else:
    print('it is not ')
