number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "**":
    print(number1 ** number2)
elif operation == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error! Division by zero.")
elif operation == "//":
    if number2 != 0:
        print(number1 // number2)
    else:
        print("Error! Division by zero.")
elif operation == "%":
    if number2 != 0:
        print(number1 % number2)
    else:
        print("Error! Division by zero.")        
else:
    print("Invalid operation!")