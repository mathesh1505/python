try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
else:
    print("Division Result:", result)
finally:
    print("This will always execute, no matter what.")
