import random

x = int(input("enter a number for the top range : "))

range_number = random.randint(1 , x)

guess = 0
while True:
    guess_number = int(input("Enter your guess : "))

    if range_number == guess_number:
        print("you got it you guessed the right function")
        guess = guess +1
        break
    else:
         if range_number>guess_number:
            print("your guess is too low try something a higher number")
            guess=guess+1
         else:
            print("you guess is too high try something a lower number ")
            guess=guess+1

print(f"you took , {guess} , try to get correct number")






