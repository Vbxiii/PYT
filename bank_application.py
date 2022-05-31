# Write a program that allows customers to:
# 1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
# 2. Log in to the program if they have an account
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. Users should be able to check their account balances.
# The program should keep running until the user decides to make it log out and/or quit.
# The account data should be stored in a dictionary that looks like this:


from ast import Pass
import random
import time


def generate_otp(n):
    otp = ""
    for _ in range(n):
        otp += str(random.choice(range(10)))
        # x = '0'
        # otp.join(x)
    return otp


# print(generate_otp(9))

data = {}
balance = 0

while True:
    user_in = input("""
    Welcome!
    press 1 to create account
    press 2 to login
    press 3 to quit: """)

    if user_in == '1':
        first_name = input('first name: ').capitalize()
        last_name = input('last name: ').capitalize()
        login_pin = int(input('choose login pin: '))
        transaction_pin = int(input('choose transaction pin: '))
        account_number = generate_otp(10)
        data[account_number] = {'first name': first_name, 'last name': last_name, 'login pin': login_pin,
                                'transaction pin': transaction_pin, 'balance': balance}

        print('processing request.....')
        time.sleep(3)
        print(
            f'welcome {first_name}  {last_name} your account number is {account_number} ')

    elif user_in == '2':
        account_number = input('Enter your account number\n:>> ')
        user_data = data.get(account_number, False)
        if user_data:
            user_selection = input(f"""
                welcome! {first_name}
                press A for deposit
                press B for withdrawal
                press C for transfer
                press D for balance""")
            # account_number = int(input('Enter your account number\n:>> '))
            # pin = int(input('Enter your pin\n:>> '))

            # while account_number:
            # if account_number and pin == account_number and login_pin:

            if user_selection == 'A':
                amount = float(input('Enter amount\n:>> '))
                current_balance = balance + amount
                data[account_number] = balance

                print(
                    f'deposit of {amount} was successful your new balance is {current_balance}')

            elif user_selection == 'B':
                amount = int(input('amount\n:>>'))
                pin = int(input('Enter transaction pin\n:>> '))

                tries = 0
                max_n_of_tries = 3

                while True:

                    if pin == transaction_pin:
                        amount - current_balance
                        data[account_number] = current_balance

                        if amount > current_balance:
                            print('insufficeint balance')
                        else:
                            print(f'withdrawal of {amount} successful')
                    else:
                        print('invalid pin')
                    tries += 1

            elif user_selection == 'C':
                withdrawal_acc = int(
                    input('Enter destinational account\n:>> '))
                withdrawal_amount = int(input('Enter amount\n:>>'))
                data[account_number] = balance

                if withdrawal_amount > data['balance']:
                    print('insufficient balance')
                else:
                    print('transfer successful')

            elif user_selection == 'D':
                print(f'Hello {first_name} your current balnce is {balance} ')

            # else:
                # print('invalid selection')
        else:
            print('invalid input, try again')

    elif user_in == '3':
        break

    else:
        print('Invalid input')


        
        
  