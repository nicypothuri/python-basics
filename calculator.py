#def calculator():
#    print('Welcome to my calculator!')

#    num1 = float(input('Enter first number:'))
#    num2 = float(input('Enter second number:'))

#    operation = input('choose an operation(Addition / Subtraction / Multiplication / Division): ')

#    if operation == 'Addition':
#        result = num1 + num2

#    elif operation == 'Subtraction':
#        result = num1 - num2

#    elif operation == 'Multiplication':
#        result = num1 * num2

#    elif operation == 'Division':
#        if num2 == 0:
#            print('Error: Division by zero is not allowed.')
#            return  
#        result = num1 / num2
#    else:
#        print('Invalid operation. Please choose from Addition, Subtraction, Multiplication, or Division.')
#        return
    
#    print('Result:', result)

#calculator()



def calculator():
    print("Welcome to my calculator!")
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
calculator()    