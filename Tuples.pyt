# A tuple is an immutable data structure that has it's elements separated by a comma, A tuple is enclosed in poaranthesis, it is ordered so it can be , it has 2 methods- count and index. A tuple is used for storing datav in a datat structure that doesn't need to be changed. It can retain duplicate values, can contain more than one data type or data structures. To create a tuple.

# A SET - is an un-ordered data-structure that has it's elements separated by a comma, enclosed in curly braces. A set cannot contain duplicate values, it is mutable

# SET METHODS 
# No1 Set method - DISCARD,REMOVE(does not work if a value is not invcluded), UNION, UPDATE, INTERSECTION
# a = {1, 2,3, 4, 5, 6}
# # a.discard(7)
# # a.remove(7)
# a.clear()
# print(a)

#  UNION
# a = {1,2,3,4,5,6}
# b = {2,4,6,8,10}
# c = a.union(b)
# print(c)

# UPDATE 
# a = {1,2,3,4,5,6}
# b = {2,4,6,8,10}
# a.update(b)
# print(a)

# INTERSECTION
a = {1,2,3,4,5,6}
b = {2,4,6,8,10}
# c = a.intersection_update(b)
a.intersection_update(b)
print(a)
