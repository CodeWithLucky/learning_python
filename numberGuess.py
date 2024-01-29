import random
randNum = random.randint(1, 10)

# print(randNum)

while(True):
    userInput = int(input("Guess a number"))
   
    if randNum>userInput:
        print("Your number is smaller")
    elif randNum<userInput and userInput<= 10:
        print("Your number is greater")
    elif randNum==userInput:
        print("Your guess is right")
        break
    elif userInput>10:
        print("You exceeded the number range")
    else:
        print("ERROR")

