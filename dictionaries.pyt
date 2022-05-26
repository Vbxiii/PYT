# A dictionary in python is a collection of data represented in key value pairs; separated by commas; un-ordered and enclosed in curly braces. Elements in the dictionary are accessed by their keys. A dictionary is mutable.The keys of a dictionary can be any immutable data-type or structure e.g strings, integers,floats,boolean,tuple. However the value of the dictionary can be any data-type or structure.

dict_A = {"A":1, "B":2, "C":3}
# print (a["c"])
dict_A["B"] = 49

# print (dict_A["B"])

# dict_A["new_key"] = "new_value"

# print(dict_A.get("A","This Key does not exist"))

# DICTIONARY METHODS : - .UPDATE , .VALUE, .KEYS, .GET
# .GET METHOD - is used to get the value of a dictionary key. If the key does not exist , the get method returns 'none' rather than the "key error" response. It is also possible to add a default value to the Get method.

# import random

# my_arr = [random.choice(range(10)) for i in range (10)]

# my_arr = [0,4,9,7,1,1,3,4,7,8,8,0,3,1,3,2,4,8,3,2,4,6,7,8,3,6,3,7,5,6,1,0,2,7,5,4,3,5,0,7,3,7,9,7,1,7,6,0,5,2]
# freq = {}

# for ele in my_arr:
#     freq[str(ele)] = freq.get(str(ele), 0) + 1
# print(freq) 


# dictionary .keys() will give us all the list of keys in a dictionary | .values() for all the values in the dictionary | .items() will give a list list of Tuples that contain keys and values.


a = {"k1" : "v1 ", "k2" : "v2", "k3" : "v3"}
for i in a: 
  print (i)

# UPDATE METHOD
# b = {"k4" : "v4", "k5" : "v5"}
# a.update(b)
# b.pop("k4")
# print(a)

# classwork - given the dictionary below, change the key called ID to employee ID
data = {"name" : "Wale",
         "city": "Silicon",
         "Salary" : "$20,000",
          "id" : "48729" }  

# data.pop("id")
data["employeeID"] = data.pop("id")
print(data)
