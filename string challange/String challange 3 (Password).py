#check if the passowrd and confirm password are same 
pass1= input('Enter the Password')
pass2= input('Renter the Passowrd')
if pass1 == pass2:
    print('It is valid Passowrd')
elif pass1.casefold() == pass2.casefold() :
    print('Please check your word and re-enter')
else:
    print('It is not working out ')