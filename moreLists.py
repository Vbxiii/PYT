# case 1
# a = [4,3,2,1,8]
# b = a
# b[3] = 7
# print (b)
# print(a)


# case2 - COPY METHOD 
# a = [4,3,2,1,8]
# b = a.copy()
# b[3] = 7
# print (b)
# print (a)

# random example of different objects
# a = [1,2,3,4]
# b = [1,2,3,4]
# print (a==b)
# print (a is b)

# append method = addition
# a = [2,3,4,5]
# b = []
# .pop method
# # b = a.pop(2)
# b.append(a.pop(2))
# print(b)

# # insert method
# a = [1,2,10,3,4]
# # insert at index() the value of ()
# a.insert(2,10)
# print(a)


# Classwork: remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# j =[ x for x in list1 if x]
# print (j)

# classwork2: write a function that generates "n" digit OTP
import random

# def generate_otp(n) :
#     otp = ""
#     for _ in range(n) :
#         otp += str(random.choice(range(10)))
#     return otp
# print(generate_otp(6))

# adding string to OTP/ generatepasscode.join as a string method
import string

def generate_otp(n) :
    """Generates n*2 length of otp"""
    otp = []
    for _ in range(3) :
        otp.append(str(random.choice(range(10))))
        otp.append(random.choice(string.ascii_letters))
    random.shuffle(otp)
    return "".join(otp)
print(generate_otp(8))