import random

choices = ['scissor', 'paper', 'rock']



userScore = 0
compScore = 0
draw = 0
for i in range(3):
    userChoice = input("Enter your choice ")
    computerChoices = random.choice(choices)

    if userChoice == computerChoices:
        draw = draw + 1
    elif userChoice == 'scissor' and computerChoices == 'paper':
        userScore = userScore + 1
    elif userChoice == 'paper' and computerChoices == 'scissor':
        compScore = compScore + 1
    elif userChoice == 'rock' and computerChoices == 'paper':
        compScore = compScore + 1
    elif userChoice == 'scissor' and computerChoices == 'rock':
        compScore = compScore + 1
    elif userChoice == 'paper' and computerChoices == 'rock':
        userScore = userScore + 1
    elif userChoice == 'rock' and computerChoices == 'scissor':
        userScore = userScore + 1
    else:
        print("ERROR")


if userScore > compScore:
    print("You won the game ")
elif userScore < compScore: 
    print("You loose the game ")
elif userScore == compScore:
    print("Game draw")


print("Your score : " , userScore)
print("Computer Score : " , compScore)
print("Draw " , draw)