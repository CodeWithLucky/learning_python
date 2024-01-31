import json
import os


datafile = "database.json"



def read_data():
    if not os.path.exists(datafile):
        return {}
    with open(datafile, 'r') as file:
        return json.load(file)
    
def write_data(data):
    with open(datafile, 'w') as file:
        json.dump(data, file, indent=4)

def create_user():

    users = read_data()

    print("Enter username: ")
    user_name = input()

    if user_name in users:
        print("Username already exists")
        return 
    password = input("Enter a password \n")
    users[user_name] = {"password" : password  , "balance" : 0.0}
    write_data(users)
    print("Account created successfully")


def login():
    users = read_data()

    print("Enter your username")
    username = input()
    print("Enter your password")
    password = input()

    balance = users[username]['balance']

    if username in users and users[username]['password'] == password:
        print(f"\n You are successfully logged in\n Your balance is {balance}\n")
        return username
    else:
        print("Your account does not exists.\n Please create one")
        return None


def deposite(user):
    users = read_data()
    print("Enter deposite amount")
    amount = float(input())

    users[user]['balance'] += amount

    write_data(users)

    print(f"You account is deposited with Rs.{amount}")

def withdraw(user):
    users = read_data()
    with_amount = int(input("How much you want to withdraw \n"))

    if users[user]['balance'] >= with_amount:
        users[user]['balance'] -= with_amount
        write_data(users)
        print(f"Your account is withdrawn with {with_amount}")

def check_balance(user):
    users = read_data
    print(f"Your current balance is: {users[user]['balance']}")


def main():
    print("__WELCOME TO NEPAL BANK__ \n")

    print("Choose the option")

    print("1. Create Account")
    print("2. Access Existing Account")
    print("3. Exit")

    user_choice = int(input())

    if user_choice == 1:
        create_user()
    elif user_choice == 2:
        user = login()
        if user:
            while True:
                print("What you want to do")
                print("\n 1.Deposite\n 2.Withdraw\n 3.Check Balance\n 4.Logout")
                make_choice = int(input())

                if(make_choice == 1):
                    deposite(user)
                elif(make_choice == 2):
                    withdraw(user)
                elif make_choice == 3:
                    check_balance(user)
                elif make_choice == 4:
                    break

    elif user_choice == 3:
        print("Are you sure you want to exit ? ")
        

main()