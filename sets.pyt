



# a = {3,4,7,8,10,17}
# b = {2,4,6,8,10,12}
# c = a.union(b)
# a.update(b)
# a.intersection(b)
# a.inertsection_update(b)
# # a.difference(b)
# a.difference_update(b)
# a.symmetric_difference(b)
# a.symmetric_difference_update(b)
# print(a)

# Classwork - students who have at least one subscription
eng = input ("Enter the total number of the students\n::>")
eng_set = set(input("Enter the roll number of the english student subscribers\n::>").split())

fre = input ("Enter the total number of the students\n::>")
fre_set = set(input("Enter the roll number of the french student subscribers\n::>").split())

print(len(fre_set.symmetric_difference(eng_set)))



