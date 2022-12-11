#program number 52

import random

# num = random.randint(1,100)
# print(num)

#program number 53
# fruits = random.choice(["Mango" , "Litchi" , "Banana" , "Pineapple" , "Apple"])
# print(fruits)

#program number 54
# computer_turn = random.choice(["h" , "t"])
# your_turn = input("Enter either head or tail (h/t) : ")
# if computer_turn==your_turn:
#     print("You win ")
# else:
#     print("You lose")
# print("computer chose the" , computer_turn)

#program number 55
# computer_turn = random.randint(1 , 5)
# your_turn = int(input("Enter your Number between 1 to 5 : "))
# if computer_turn==your_turn:
#     print("Well Done ")
# elif computer_turn>your_turn:
#     print("Too low try something high")
#     your_turn = int(input("Guess again : "))
#     if your_turn==computer_turn:
#         print("Correct")
#     else:
#         print("You lose")
# elif computer_turn<your_turn:
#     print("too high try something a lower number ")
#     your_turn = int(input("Guess again : "))
#     if your_turn==computer_turn:
#         print("Correct")
#     else:
#         print("You lose")
# print("Computer choose" , computer_turn)

#program number 56
# computer_turn = random.randint(1 ,10)
# correct = False
# while correct==False:
#     your_turn = int(input("Enter a number between 0 to 10 : "))
#     if your_turn==computer_turn:
#         correct = True
# print("computer chose" , computer_turn)

#program number 57
# computer_turn = random.randint(1 ,10)
# correct = False
# while correct==False:
#     your_turn = int(input("Enter a number between 0 to 10 : "))
#     if your_turn==computer_turn:
#         correct = True
#     elif(your_turn>computer_turn):
#         print("Too high enter a lower number")
#     else:
#         print("Too low try something higher ")
# print("computer choose" , computer_turn)

#program number 58
# score = 0
# for i in range(1 , 6):
#     num1 = random.randint(1 , 50)
#     num2 = random.randint(1 , 50)
#     correct=num1 + num2
#     print(num1 ,"+" ,num2,"= ??"  )
#     answer = int(input("Enter your Answer : "))
#     print()
#     if answer==correct:
#         score = score + 1
# print("You scored" , score , "out of 5")

#program number 59
# color = random.choice(["red" , "blue" , "green" , "white" , "pink"])
# print("Select from red , blue , green , pink , white ")
# tryagain = True
# while tryagain==True:
#     theirchoice = input("Enter a color : \n")
#     theirchoice = theirchoice.lower()
#     if color==theirchoice:
#         print("Well Done")
#         tryagain=False
#     elif theirchoice=="red":
#         print("I bet you are seeing RED right now!!")
#     elif theirchoice=="blue":
#         print("Don't feel Blue ")
#     elif theirchoice=="green":
#         print("I bet you are green with envy right now and shining like an emreald ")
#     elif theirchoice=="pink":
#         print("Shame on you are not feeling PINK , as you got it wrong!!")

