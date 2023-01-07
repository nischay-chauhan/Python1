#program number 118
# def ask_value():
#     num = int(input("Enter a number : "))
#     return num

# def count(num):
#     n=1
#     while n<=num:
#         print(n)
#         n = n + 1

# def main():
#     num = ask_value()
#     count(num)

# main()

#program number 119
# import random


# def pick_num():
#     low = int(input("Enter the bottom of the range : "))
#     high = int(input("Enter the top of the range : "))
#     comp_num = random.randint(low,high)
#     return comp_num

# def first_guess():
#     print("I am thinking of a number... ")
#     guess = int(input("What am I thinking of : "))
#     return guess

# def check_annswer(comp_num , guess):
#     while True:
#         if comp_num == guess:
#             print("corret, You win")
#             break
#         elif comp_num>guess:
#             guess = int(input("Too low,Try again : ")) 
#         else:
#             guess = int(input("Too high, Try again : "))

# def main():
#     comp_num = pick_num()
#     guess = first_guess()
#     check_annswer(comp_num , guess)

# main()

#program number 120
import random


def addition():
    num1 = random.randint(1 , 25)
    num2 = random.randint(25 , 50)
    print(num1 , "+" , num2 , "= " )
    user_answer = int(input("Enter your answer : "))
    actual_answer = num1 + num2
    answers = (user_answer , actual_answer)
    return answers

def subtraction():
    num3 = random.randint(25 , 50)
    num4 = random.randint(1 , 25)
    print(num3 , "-" , num4 ,"= " )
    user_answwer = int(input("Enter your answer : "))
    actual_answer = num3 - num4
    answers2 = num3 - num4
    return answers2

def new_func():
    num3 = random.randint(1 , 25)
    return num3

def check_answers(user_answer , actual_answers):
    if user_answer==actual_answers:
        print("correct ")
    else:
        print("incorrect , the actual answer is" , actual_answers)

def main():
    print("1) Addition ")
    print("2) Substraction ")
    selection = int(input("Choose between 1 and 2 operator : "))
    if selection==1:
        user_answer , actual_answer, = addition()
        check_answers(user_answer , actual_answer) 
    elif selection== 2:
        user_answer , actual_answer, = subtraction()
        check_answers(user_answer , actual_answer)
    else:
        print("Incorrect answer ")
main ()


# #program number 121
# def add_name():
#     names = []

#     name = input("Enter any name : ")
#     names.append(name)


