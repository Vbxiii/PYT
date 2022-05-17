# h = 1 
# while h <= 10:
#     h += 1
#     print(h)


import random

# print("Guess the computer's choice to winthe prize.")
# a = [1,2,3,4,5,6,7]

# # random.shuffle(a)
# # random.sample(a,3)
# random.shuffle(a)
# trial = 3
# score = 0

# while trial >0:
#     print("Select a number from", a)
#     com_choice = random.choice(a)
#     user = int(input("Your choice\n:>"))
#     if user == com_choice:
#         print("You Win!")
#         score+=2
#         trial+=1
#         print(f"You've won an extra trial")
#         print(f"{trial} trial(s) left")

#     else:
#         if user > com_choice:
#            print("Too High!")
#         else:
#            print("Too Low")
#         trial -=1
#         print(f"{trial} trial(s) left")
        
# print(f"\nYou scored {score} points")
# print("Game over ):")

options = ["r", "p", "s"]
trial = 3
score = 0

while trial >0:
    print ("Select R for rock, P for paper and S for scissors.")
    com_choice = random.choice(options)
    player_choice = input (">").lower()
    if player_choice in options:

        if player_choice == options[0] and com_choice == options[2]:
            print("You win")
            print("computer choose, com_choice")
            trial += 1
            score += 2
        elif player_choice ==options[2] and com_choice == options[1]:
            print("You win")
            print("computer choose", com_choice)
            trial += 1
            score += 2
        elif player_choice == options[1] and com_choice == options[0]:
             print("You win")
             print("compter choose", com_choice)
             trial += 1
             score += 2
        elif player_choice == com_choice:
             print("It's a tie")
        else:
            print("You Lose")
            print("computer choose", com_choice.title())
            trial -= 1
    else:
        print('You entered an Invalid input')
        trial -= 1
    print (f'You have {trial} trials left')
print("Game Over!")        
print("You Scored", score)        

       
