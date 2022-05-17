# new_string = "This is a string."

# new_doc_string = """This is a nice string
# and it can write on multiple line
# e.g see easy """

# string1 = "This is a string"
# string2 = "I love this string"

# print(string1 + string2)
# print(string1 + " " + string2)
# print(string1, string2)

# print(string1[-1])

# number = 984
# print(number[-1])

# # a[start: stop: step]
# print(string1 [3:13:2])

# FORMATTING
# name = "Emmanuel"
# print(f"my name is {name}")

# name = input("Enter your name: ")

# print(f"""Welcome , {name}.

# You have signed up successfully.

# Cheers,
# Newlife Team.""")


# c/w write a program that takes first name and last name from the user. Generate a username that has the first three letters of the last name and the last 2 letters of the first name. Print a welcome message to the user notifying them of their new username.

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# user_name = (first_name[-2:] + last_name[:3])
# print(f"""Welcome, {first_name}
# Your username is {user_name}""")
# 
# Escape Character \
# print("The man said \"You do what youy have to do, so you can do what you want to do.\" I hope you have been inspired")
# print('The man said \"You do what youy have to do, so you can do what you want to do.\" I hope you have been inspired')
# print("This is a dog.\nHis name is Jack.")

# String methods
# name = input("Enter your name:\::>>")
# print(name.upper())

#  write a program that asks the user for a word to search for in a sequence of string. Search for the word and return the number of occurences and highlight the places where the words were found.

text = """An alternative is designed development, in which high-level insight into the problem can make the programming much easier. In this case, the insight is that a Time object is really a three-digit number in base 60"""

search_for = input(">").lower()
print(f"{text.lower().count(search_for)} result(s) found")
print(text.lower().replace(search_for, search_for.upper()))