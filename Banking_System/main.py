import random


new_balance = 0.00
balance = 0.0
account_number = random.randint(123456789, 987654321)

db = [
    {'1' : {'name' : "laxman" , "address" : "banepa" , "account_number" : account_number , "balance" : balance},
     '2' : {'name' : "Rahul" , "address" : "banepa" , "account_number" : account_number , "balance" : balance},
     '3' : {'name' : "Pemba" , "address" : "banepa" , "account_number" : account_number , "balance" : balance},
     '4' : {'name' : "Nishan" , "address" : "banepa" , "account_number" : account_number , "balance" : balance}
     }
]


def login(name):
   
    for person in db:
        for key , individual in person.items():
            if name == individual['name']:
                print(f"You are successfully loged in..\n Your account number is : {account_number}")
                break
            else:
               print("Sorry your name does not match")

    
def deposite():
    print("Enter amount for deposite: ")
    amount = int(input())
    new_balance = amount + balance
    print(f"Your account has been credited with Amount : Rs.{amount} \n Your new balance is Rs.{new_balance}")


def withdraw():
    print("How much money you want to withdraw")
    with_amt = int(input())
    new_balance = balance - with_amt
    print(f"You have successfully withdrawn Amount: Rs.{with_amt} \n Your new balance is Rs.{new_balance}")

def check_balance():
    print("Your balance is Rs.{balance}")


print("..Welcome to Bank of Luck..")
print("Please Enter your name to login : ")
login_name = input()

login(login_name)

if login:
    print("What you want to do: \n 1.Deposite \n 2.Withdraw \n 3.Check Balance")
    operation = int(input())
    if operation == 1:
        deposite()
    
    elif operation == 2:
        withdraw()
    elif operation == 3:
        check_balance()












