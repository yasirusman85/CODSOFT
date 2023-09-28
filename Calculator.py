# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Prompt the user for input
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if the input is a valid choice
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        if result == "Cannot divide by zero":
            print(result)
        else:
            print("Result:", result)
else:
    print("Invalid input. Please select a valid operation (1/2/3/4).")
