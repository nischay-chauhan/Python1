#program number 80
# first_name = input("Enter your first name : ")
# length = len(first_name)
# print("The length of firstname is" , length , "digit")
# sur_name = input("ENter your surname : ")
# lenght2 = len(sur_name)
# print("the length of surname is" , lenght2 , "digit")
# name = first_name + " " + sur_name
# print("your full name is " , name)
# print("your full name has" , len(name) , "digits")

#program number 81
# language = input("Enter your favourite language : \n")
# for letter in language:
#     print(letter , end="-")

#program number 82
# poem = '''You are the shadow to my light can you see it... another star just fade away'''
# print(poem)
# start = int(input("Enter a starting number : "))
# end = int(input("Enter a ending number : "))
# print(poem[start:end])

#program number 83
# msg = input("Enter a world in upper case : ")
# tryagain = False
# while tryagain==False:
#     if msg.isupper():
#         print("Thank you")
#         tryagain=True
#     else:
#         print("try again")
#         msg = input("Enter the word in upper cases : ")

#program number 84
# postcode = input("Enter your postcode")
# start = postcode[0:2]
# print(start.upper()) 

#program number 85
# name = input("Enter your Name : ")
# count = 0
# name = name.lower()
# for x in name:
#     if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
#         count = count + 1
# print("your name has " , count , "vowels in it")

#program number 86
# pswd1 = input("Entetr a password : ")
# if pswd1==pswd2:
#     print("Thank you , your password is correct ")
# elif pswd1.lower()==pswd2.lower():
#     print("They must be the same case ")
# else:
#     print("Incorrect ")

#program number 87
# word = input("Enter a word : ")
# length = len(word)
# num = 1
# for x in word:
#     position = length-num
#     letter = word[position]
#     print(letter)
#     num = num + 1