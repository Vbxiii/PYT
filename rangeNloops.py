# A loop is a way of going through a block of code for a period of time. 
# There is a "for loop" which goes over a block of code over a period of time or for a range.
# Range is a function that gives a number that falls within a start point and an end point
# 


# for i in range(10):
#       if i == 5:
#         # break
#         continue
#       print(i)



# write a program to print all the odd numbers between 90 and 120
# a = 0
# for i in range (90, 120):
#     if i%2 == 1:
#         a += 1
#         print(i)
# print(" ")
# print(a)
# print(" ")

# Given an array of integers, print all the multiples of 5 and 3 [1,2,3,4,15,22,21,33,50,55,72,66,95]

# 

    
# assignment: write a function that takes in an integer and returns either True or False if it is a prime number.
n=int(input("Enter number: ")) 
k=0 
for i in range(2,n//2+1): 
    if(n%i==0): 
        k=k+1 
if(k<=0): 
    print("Number is a prime number") 
else: 
    print("Not a Prime Number") 

# Correction
