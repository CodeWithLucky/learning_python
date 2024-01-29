task = []

print("1. Add \n 2. Remove")
operation = int(input())


if operation == 1:
    numTask = int(input("Enter how many task you want to add:  "))

    print("Enter tasks")

    for i in range(numTask):
        userInput  = input()
        task.append(userInput)
if operation == 2:
    remTask = input("Enter what you want to remove  ")
    task.remove(remTask)

print(task)
