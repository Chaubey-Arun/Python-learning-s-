email = input('Enter the Email id')
postion = email.index('@')#we cand use 'email.find('@')
userid= email[0:postion:]
domain = email[postion+1:]
print('user id -',userid ,'\n' ,'Domain name -',domain)