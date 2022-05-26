# LISTS - A collection of data enclosed in [] mwhich each of it's elements separated with a comma "," it is ordered so each of it's elements can be accessed by it's index. It is mutable anc can contain anytype of data type/ structure

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# b[3] = 82
# print(b)


# a = [1,2,3,4,5,6,7]
# #    0,1,2,3,4,5,6
# # a[stepstart:stop:]
# a[2:5] 
# for i in a:
#     print(i)

# a=[expression for item in range]
# a =[(x)** for x in range(10)]

# a=>[0**,1**,2**,3**,4**,5**,6**,7**,8**,9**]

# CLasswork
# in the a list below, add 9 +8 
a = [1,2,4,7,[5,9,[8,7],4],3,7]
b = a[4][1] + a[4][2][0]
print (b)

import random 
a =  [i for i in range (10)]

random.shufflle(a)
print(a)

# print(sorted(a, reverse = true))

a.reverse()
print(a)

