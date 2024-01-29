task = []

numTask = int(input("Enter how many task you want to add:  "))

print("Enter tasks  ")

for i in range(numTask):
    userInput = input()
    task.append(userInput)

print("1. Add \n 2. Remove")
operation = int(input())
if(operation == 1):
    newTask = input("Enter new task  ")
    task.append(newTask)
elif(operation == 2):
    remTask = input("Which you want to remove  ")  
    task.remove(remTask)
else:
    print("Invalid request ")

print(task)