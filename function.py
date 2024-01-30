#function

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))




    def sum(a=first_number, b=second_number):
        return a+b

    def diff(a=first_number, b=second_number):
        return a-b

    def multi(a=first_number, b=second_number):
        return a*b


    def div(a=first_number, b=second_number):
        return (a/b)

    


    print("Choose operation \n 1.ADD \n 2.Difference \n 3.Multiply \n 4.Divide")
    operation = int(input())

    try:
        if(operation==1):
            addition = sum()
            print(addition)
        elif(operation==2):
            subtraction = diff()
            print(subtraction)
        elif(operation==3):
            multiplication = multi()
            print(multiplication)
        elif(operation==4):
            try:
                division = div()
                print(division)
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Invalid operation ")
    except ValueError as e:
        print(e)
except ValueError as e:
    print("Invalid input")
