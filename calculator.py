def calculator():
    print("Welcome to my calculator!")
    print("These are the operations you can perform: add, sub, multiply, divide, quit")
    while True:
        print("What would you like to do?")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation(add / sub / multiply / divide / quit):")
        if operation == "quit":
            print("Goodbye!")
            break
        elif operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                print("Error: Can't divide by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation, Please try again.")
            continue
        print("Result:", result)
        if input("Do you want to calculate again? (yes/quit):").lower() == "yes":
            continue
        else:
            print("Goodbye!")
            break
calculator()    