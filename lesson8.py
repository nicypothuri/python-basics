#ERROR HANDLING
try:
    num = float(input("Enter a number:"))
    result = 10 / num
    print("10 divided by", num, "is", result)
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Thank you using the calculator!")