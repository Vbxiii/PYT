# factorial (n) 5 * f(n-1), 4* f(n-1), 3* f(n-1), 2*f(n-1), 1*f(n-1) ; n becomes 0 at a point and loops back because 0 returns 1
# def factorial(n):
#     if n==1:
#         return 1
#     if n == 0:
#         return 1
#     recurse = n * factorial(n-1)
#     print(recurse)
#     return recurse


# factorial(5)

# CONTROL STRUCTURES

# print('x')
# if  4 > 5:
#     print(7)

# print(4)

# class example using students scores to show their grades with the else if (elif) function
# score = int(input("Enter your exam score:\n:>"))

# if score <= 100:
#   if score >= 90:
#      print('A')
#   elif score >= 80:
#      print('B')
#   elif score >= 70:
#       print('C')
#   elif score >= 60:
#      print('D')
#   elif score >= 50:
#      print('E')
#   elif score >= 40:
#      print('F')
#   else:
#      print('To repeat this class')
# else:
#      print('Outstanding')

# my_str = " this is a lovely string"
# a = list(map(lambda f:f.upper(), my_str))
# print("".join(a))
   
import random

# print("Guess the computer's choice to winthe prize.")
# a = [1,2,3,4,5,6,7]
# print("Select a number from", a)
# # random.shuffle(a)
# # random.sample(a,3)
# random.shuffle(a)
# com_choice = random.choice(a)
# user = int(input("Your choice\n:>"))
# if user == com_choice:
#     print("You Win!")
# else:
#     if user > com_choice:
#         print("Too High!")
#     else:
#         print("Too Low")
#     print("You Lose!")


# ROCK - PAPER - SCISSORS

# print ("Guess Rock or Paper or Scissors")
# rps = ["rock", "paper", "scissors"]
# print("select an option from", rps)
# random.shuffle(rps)
# com_choice = random.choice(rps)
# user_choice = input('pick from the choice above: ').lower()
# if user == com_choice:
#     print("You win!")
# else:

# if com_choice == user_choice:
#     print('Both players tie, try agin!')
# elif user_choice == "rock" :
#     if com_choice == 'scissors':
#         print('Rock smashes scissors,You WIN!')
#     else:
#      print ('paper covers rock, you lose!')
# elif com_choice == 'rock':
#     if user_choice == 'paper':
#      print('paper covers rock, you won!')
#     else:
#        print ('scissors cuts paper,try again')
# elif user_choice == 'scissors':
#     if com_choice == 'paper':
#      print("Scissors cuts paper! You win!")
#     else :
#      print("Rock smashes scissors, you lose!")

# CORRECTION
options = ["r", "p", "s"]
print ("Select R for rock, P for paper and S for scissors.")
com_choice = random.choice(options)
player_choice = input (">").lower()
if player_choice in options:
    if player_choice == options[0] and com_choice == options[2]:
        print("You win")
        print("computer choose, com_choice")
    elif player_choice ==options[2] and com_choice == options[1]:
        print("You win")
        print("computer choose", com_choice)
    elif player_choice == options[1] and com_choice == options[0]:
        print("You win")
        print("compter choose", com_choice)
    elif player_choice == com_choice:
        print("It's a tie")
    else:
        print("You Lose")
        print("computer choose", com_choice.title())
else:
    print('Invalid input') 
