#checking a string is a palindrone by using string Method 
str1= input('Enter to check Palindrome -')
n=len(str1)
str2 = str1[::-1]
if (str1 == str2):
    print('Palindrome')
else:
    print('it is not ')
