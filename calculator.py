firstNumber =  int(input("Enter first number"))
secondNumber = int(input("Enter second number"))

print("Choose which operation you want to perform")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

operation = input()


if(operation == "1"):
    print("Sum of your numbers is: " , (firstNumber + secondNumber))
elif(operation == "2"):
     print("Diff of your numbers is: " , (firstNumber - secondNumber))
elif(operation == "3"):
     print("Multiplication is: " , (firstNumber * secondNumber))
elif(operation == "4"):
     print("Division is: " , (firstNumber/secondNumber))
else:
     print("Invalid input")