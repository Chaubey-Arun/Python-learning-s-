s1= input("Enter string 1")
s2 = input("Enter string 2")
if len(s1)!=len(s2):
    print("not anagram")
else: 
    for i in s1:
        if i  not in  s2:
            print("it is not anagram")
            break;
    else:
         print('it is a Anagram')
