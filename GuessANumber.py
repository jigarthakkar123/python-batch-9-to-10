import random

num=random.randint(1,30)

while True:

    guess=int(input("Guess A Number Between 1 to 30 : "))
    if guess==num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed A Greater Number")
    elif guess<num:
        print("You Guessed Smaller Number")
