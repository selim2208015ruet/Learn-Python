try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero!")