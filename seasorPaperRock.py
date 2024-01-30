import random

choices = ['scissor', 'paper', 'rock']



userScore = 0
compScore = 0
draw = 0
for i in range(3):
    userChoice = input("Enter your choice : scissor  paper  rock ").lower()
    computerChoices = random.choice(choices)


    if userChoice == computerChoices:
        draw = draw + 1
    elif (userChoice == 'scissor' and computerChoices == 'paper') or (userChoice == 'paper' and computerChoices == 'rock') or (userChoice == 'rock' and computerChoices == 'scissor'):
        userScore = userScore + 1
    else:
        compScore = compScore + 1



if userScore > compScore:
    print("You won the game ")
elif userScore < compScore: 
    print("You loose the game ")
elif userScore == compScore:
    print("Game draw")


print(f"Your score : {userScore}" )
print(f"Computer Score : {compScore}" )
print(f"Draw:  {draw}" )