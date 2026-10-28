
# Program 3: Exception Handling
# Divides two numbers and handles bad input safely.

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
except ValueError:
    print("Error: that wasn't a valid number.")
except ZeroDivisionError:
    print("Error: you can't divide by zero.")
else:
    print(f"{a} / {b} = {result:.2f}")
finally:
    print("Thanks for using the calculator!")
