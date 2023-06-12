def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Welcome to the Calculator!")

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Calculator closed.")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)

    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)
        
    elif choice == '4':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice. Please try again.")

# Welcome to the Calculator!
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice (1-5): 3
# Enter the first number: 10
# Enter the second number: 20
# Result: 200.0

