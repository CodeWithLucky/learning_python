import os
import json

database = 'data.json'
while True:

    def read_data():
        if not os.path.exists(database):
            return {}
        with open(database, 'r') as file:
            return json.load(file)


    def write_data(data):
        with open(database, 'w') as file:
            json.dump(data, file, indent=4)

    def create_account():
        users = read_data()
        print("Enter username ")
        username = input()

        if username in users:
            print("Account already exists ")
            return
        password = input("Enter a password: \n")
        users[username] = {"password" : password , "balance" : 0.0}
        write_data(users)
        print("Account created successfully..\n")

    def login():
        users = read_data()
        print("Enter username:")
        username = input()
        print("Enter password:")
        password = input()

        if username in users and users[username]['password'] == password:
            print("Successfully logged in.\n")
            return username
        else:
            print("Account does not exist.\nPlease create account\n")
            return None


    def deposite(user):
        users = read_data()
        print("How much you want to deposite: ")
        deposite_amount = float(input())
        users[user]['balance'] += deposite_amount
        write_data(users)
        print(f"Your account is deposited with Rs.{deposite_amount}. Your new balance is Rs.{users[user]['balance']}\n")

    def withdraw(user):
        users = read_data()
        print("How much amount you want to withdraw: ")
        with_amount =  int(input())
        users[user]['balance'] -= with_amount
        write_data(users)
        print(f"Your account is debited with Rs.{with_amount}. New balance is {users[user]['balance']}\n")

    def check_balance(user):
        users = read_data()
        print(f"Current balance is: {users[user]['balance']}")

    def edit_account(user):
        users = read_data()
        print("What you want to update..")
        print("\n1.Username\n2.Password\n3.Balance")
        update_option = int(input())
        if update_option == 1:
            print("Enter new username: ")
            new_username = input()
            users[new_username] = users.pop(user)
            write_data(users)
        elif update_option == 2:
            print("Enter new password: ")
            new_password = input()
            users[user]['password'] = new_password
            write_data(users)
            print("password successully updated..")

    def view_detail(user):
        users = read_data()
        print(f"Your password: {users[user]['password']}")
        print(f"Your balance: {users[user]['balance']}\n")

    def main():
        print("__WELCOME TO BANK OF ITB__")
        print("What you want to do:")
        print("\n 1.Create Account\n 2.Access Account")

        first_choice = int(input())

        if(first_choice == 1):
            create_account()
        elif first_choice == 2:
            user = login()
            if user:
                while True:
                    print("Choose one operation")
                    print("\n 1.Deposite\n 2.Withdraw\n 3.Check Balance\n 4.Edit Profile\n 5.View Profile\n 6.Logout ")
                    operation = int(input())
                    if operation == 1: 
                        deposite(user)
                    elif operation == 2:
                        withdraw(user)
                    elif operation == 3:
                        check_balance(user)
                    elif operation == 4:
                        edit_account(user)
                    elif operation == 5:
                        view_detail(user)
                    elif operation == 6:
                        break

    main()