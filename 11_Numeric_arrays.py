#program number 88
from array import *

# nums = array('i' , [])
# for i in range(0 , 5):
#     num = int(input("Enter your number : "))
#     nums.append(num)
# nums = sorted(nums)
# nums.reverse()
# print(nums)

#program number 89
# from array import *
# import random

# nums = array('i' , [])
# for i in range( 0, 5):
#     num = int(random.randint(1, 50))
#     nums.append(num)
# nums = sorted(nums)

# for i in nums:
#     print(i)

#program number 90
# from array import *

# nums = array('i' , [])
# while len(nums)<5:
#     for i in range(0 ,5):
#         num = int(input("Enter your number : "))
#         if num<=20 and num>=10:
#             nums.append(num)
            
#         else:
#             print("Enter within the range")
#     for i in nums:
#         print(i)

#program number 91
# from array import *

# nums = array('i' , [6 , 8 , 3 , 3 , 2])
# for i in nums:
#     print(i)
# num = int(input("Enter your Number : "))
# if nums.count(num)==1:
#     print("Your number appeared one time")
# else:
#     print("you number came" , nums.count(num) , "times")

#program number 92
# from array import *
# import random 

# nums1 = array('i' , [])
# for i in range(0 , 5):
#     num = random.randint(1 , 50)
#     nums1.append(num)
# for i in nums1:
#     print(i)

# nums2 = array('i' , [])
# for i in range(0 , 3):
#     numo = int(input("Enter Your Number : "))
#     nums2.append(numo)
# for i in nums2:
#     print(i)

# nums1.extend(nums2)
# num1 = sorted(nums1)
# for i in nums1:
#     print(i)

#program number 93
# from array import *

# nums = array('i' , [])
# for i in range(0 , 5):
#     num = int(input("Enter your Number : "))
#     nums.append(num)
# nums = sorted(nums)
# for i in nums:
#     print(i)
# num = int(input("Select a Number from the array : "))
# if num in nums:
#     nums.remove(num)
#     num2 = array('i' , [])
#     num2.append(num)
#     print(nums)
#     print(num2)
# else:
#     print("That is not a value innthe array")

#program number 94
# from array import *

# nums = array('i' , [4 , 6 , 5 , 2 , 1])
# for i in nums:
#     print(i)

# num = int(input("Select one number ; "))

# while True:
#     if num in nums:
#         print("This is in position" , nums.index(num))
#         break
#     else:
#         print("Not in array")
#         num = int(int(input("Select one numbers")))

#program number 95
# from array import *
# import math

# nums = array('f' , [34.75 , 20.36,45.21,96.10,20.00])
# while True:
#     num = int(input("Enter a number between 2 and 5 : "))
#     if num<2 or num>5:
#         print("Incorrect value , Try again.")
#     else:
#         break
# for i in range(0 , 5):
#     ans = nums[i]/num
#     print(round(ans , 2))


