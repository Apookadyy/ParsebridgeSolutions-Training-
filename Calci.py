

import math  # for sqrt() and log10()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot perform modulus with zero!"
    return x % y

def exponent(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Cannot perform floor division with zero!"
    return x // y

def square_root(x):
    if x < 0:
        return "Cannot find square root of a negative number!"
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        return "Logarithm undefined for zero or negative numbers!"
    return math.log10(x)

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponent (x^y)")
print("7. Floor Division")
print("8. Square Root")
print("9. Logarithm (base 10)")

choice = input("Enter choice (1-9): ")

if choice == '8':
    num = float(input("Enter a number: "))
    print("Result:", square_root(num))
elif choice == '9':
    num = float(input("Enter a number: "))
    print("Result:", logarithm(num))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    elif choice == '6':
        print("Result:", exponent(num1, num2))
    elif choice == '7':
        print("Result:", floor_divide(num1, num2))
    else:
        print("Invalid input")
