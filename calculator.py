
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit")

    while True:
        try:
            num1 = input("\nEnter first number (or type 'exit'): ")
            if num1.lower() == "exit":
                print("Exiting calculator. Goodbye!")
                break
            num1 = float(num1)

            operator = input("Enter operation (+, -, *, /): ")

            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")

calculator()
