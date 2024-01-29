import random
n = random.randint(1,10)
guess = 0 
while guess!= n:
    guess= int(input("Guess a Number"))
    if guess<n:
        print("Number is less than thought value")
    elif guess>n:
        print("Number is greater than thought value")
    else:
        print("You Guess it right")