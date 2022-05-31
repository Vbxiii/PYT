# Using the game from while loops, create a dictionary that stores player highscores


import random

# data = {}

# print("Guess the computer's choice to win the prize.")
# a = [1,2,3,4,5,6,7]


# while True:
#     username = input("Username:\n:>>")
#     trial = 3
#     score = 0


#     while trial >0:
#         random.shuffle(a)
#         print("\nSelect a number from", a)
#         com_choice= random.choice(a)
#         user = int(input("Your choice\n:>"))
#         if user == com_choice:
#             print("You win")
#             score+=2
#             trial+=1
#             print(f"You have won an extra trial")
#             print(f"{trial} trial(s) left")

#         else:
#             if user > com_choice:
#                 print("Too high")
#             else:
#                 print("Too low")
#             trial-=1
#             print(f"{trial} trial(s) left")

    # prev_score = data.get(username, 0)
#     if score > prev_score:
#         print("You just beat your previous high score!🎉🎉")
#         data[username]=score

#     print(f"\nYou scored {score} points")       
#     print("Game over ):")

#     choice = input("Play again?Y/n:\n>").lower()
#     if choice == "n":
#         break        
            
# print(data)


# data {}
# print("Welcome to Rock, Paper Scissors", "Press enter to create a username")


# options = ["r", "p", "s"]
# trial = 3
# score = 0

# while trial >0:
#     print ("Select R for rock, P for paper and S for scissors.")
#     com_choice = random.choice(options)
#     player_choice = input (">").lower()
#     if player_choice in options:

#         if player_choice == options[0] and com_choice == options[2]:
#             print("You win")
#             print("computer choose, com_choice")
#             trial += 1
#             score += 2
#         elif player_choice ==options[2] and com_choice == options[1]:
#             print("You win")
#             print("computer choose", com_choice)
#             trial += 1
#             score += 2
#         elif player_choice == options[1] and com_choice == options[0]:
#              print("You win")
#              print("compter choose", com_choice)
#              trial += 1
#              score += 2
#         elif player_choice == com_choice:
#              print("It's a tie")
#         else:
#             print("You Lose")
#             print("computer choose", com_choice.title())
#             trial -= 1
#     else:
#         print('You entered an Invalid input')
#         trial -= 1
#     print (f'You have {trial} trials left')
# print("Game Over!")        
# print("You Scored", score)



# import random

# a = {3, 4, 7, 8, 10, 17}
# b = {2, 4, 6, 8, 10, 12}

# c = a.union(b)
# a.intersection_update(b)
# print(sorted(a))
# a.difference_update(b)
# print(a)

# c = (a.difference(b)).union(b.difference(a))
# print(c)


# eng = input('enter total number of the students: ')
# eng_set = set(
#     input('enter the roll numbers of the englis subscribers \n ::>').split())


# frn = input('enter total number of the students: ')
# frn_set = set(
#     input('enter the roll numbers of the englis subscribers \n ::>').split())


# print(len(frn_set.symmetric_difference(eng_set)))


# ext = {
#     'a': 1,
#     'e': 2,
#     'c': 4
# }
# ext['new key'] = {
#     'job': False,
#     'married': True
# }
# print(ext)


# my_arr = [0, 4, 9, 7, 1,
#           1, 3, 4, 7, 8, 8, 0, 3, 1,
#           3, 2, 4, 8, 3, 2, 4, 6, 7, 8, 3, 6, 3, 7, 5, 6, 1, 0,
#           2, 7, 5, 4, 3, 5, 0, 7, 3, 7, 9, 7, 1, 7, 6, 0, 5, 2]

# my_arr = [random.choice(range(10)) for i in range(10)]


# freq = {}

# for ele in my_arr:
#     freq[str(ele)] = freq.get(str(ele), 0) + 1

# print(freq)
# for ele in set(my_arr):
#     freq[ele] = my_arr.count(ele)
# print(freq.items())




def play_game():
    print('Rock, Paper, scissors')

    rps = ['rock', 'paper', 'scissors']

    trial = 3
    score = 0
    while trial > 0:
        user = input(f'select from the options{rps}: ').lower()
        random.shuffle(rps)
        com_choice = random.choice(rps)
        if com_choice == 'rock' and user == 'paper':
            print('you won')
            print(f'you have{trial} trial(s) left')
            trial += 1
            score += 2
        elif com_choice == 'paper' and user == 'rock':
            print('you won')
            print(f'you have {trial} trial(s) left')
            trial += 1
            score += 2
        elif com_choice == 'paper' and user == 'scissors':
            print('you won')
            print(f'you have {trial} trial(s) left')
            trial += 1
            score += 2

        elif com_choice == user:
            print('tie, nobody won, try again.')
        else:
            print("you lost")
            print(f'you have {trial} trial(s) left')
            trial -= 1
            score -= 1
    print('game over')
    return score


def generate_otp(n):
    otp = ""
    for _ in range(n):
        otp += str(random.choice(range(10)))
    return otp


# print(generate_otp(6))

data = {}

while True:
    u_input = input('welcome! press 1 to signup anddd 2 to login\n: ')
    if u_input == '1':
        username = input('Enter username\n: ')
        user_id = generate_otp(6)
        data[user_id] = {'name': username, 'score': 0}
        print(f'hello! {username} your unique id is {user_id}')

    elif u_input == '2':
        user_id = input('Enter your unique id: ')
        user_data = data.get(user_id, False)
        if user_data:
            play_game()
        else:
            print("Invalid user id")


            
            
            


