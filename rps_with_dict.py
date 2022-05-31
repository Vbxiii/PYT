# RPs with dictionary correction
from moreLists import generate_otp
from more_dictionaries import play_game

import random
import time
data = {}

def generate_otp(n):






def play_game():





print("*"*31)
print("Welcome to Rock, Paper, Scissors.")
print("*"*31)

while True:
    print("what would you like to do?\n1. Login\n2. Sign up\n3. QUit")
    user_input = input("::>")

    if user_input =="1":
        print("\nPlease enter your identification number.")
        user_id = input("::>")
        user_data = data.get(user_id, False)
        if user_data:
            score = play_game()
            if score > user_data["score"]:
                user_data["score"] = score
                print("Yaay!!! 🎉🎉 ")
                print("You have a new high score. \n")
        else:
            print("\nInvalid dentification number")
    elif user_input == "2":
        print("Please enter your name")
        name = input("::>")
        user_id = generate_otp(6)
        data[user_id] = {} = {"name": name,
                                "score": 0}
        print("Creating account...")
        time.sleep(3)
        print("Completing setup...")
        time.sleep(2)
        print(f"\nWelcome {name}!\nYour account had been created and activated. Your user id is {user_id}\nCheers\nRPS Support. \n")
    elif 

