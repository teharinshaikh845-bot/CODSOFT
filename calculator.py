# Simple Calculator Program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    result = num1 + num2
    print("Result:", result)

elif choice == "-":
    result = num1 - num2
    print("Result:", result)

elif choice == "*":
    result = num1 * num2
    print("Result:", result)

elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operation selected")
