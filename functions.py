# FUNCTIONS
# def test_function():
#     print(4*2+2)

# test_function()


# def fun2(n:int): 
#     print(n**2)

    
# fun2(4)

# def fun3 (a,b,c)
#     print (a,b,c)


# fun3(1,2,3)
# fun3(a=3, b=1, c=3)


# fun3(2, b=3, c=1)



# print(test_function)

# def fun2(n:int): 
    
    # print('I am running')
    # return n**2
    # print ('I just ran')

# print (fun2(4)) 


# classwork- create a function that calculates the mean for any given array of intergers /floats and write a program that takes input from the user, separeated by a comma and calculate the mean using the function. Return your answer to 2 deicmal places.


def mean(arr):
    mean_value = sum(arr)/len(arr)
    return round(mean_value, 2)

    
print("Calculate your mean")
print("Enter your mean values")
vals = input(":>").split(',')
print(vals)
mapped = list(map(int,vals))

print(mean(mapped))

print(mean([2,23,445,21]))