while True:

    num1 = input("Enter first number (or exit): ")

    if num1.lower() == "exit":
        print("Calculator closed.")
        break

    num1 = float(num1)

    operator = input("Enter operator (+, -, *, /): ")

    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    else:
        result = "Invalid operator"

    print("Result:", result)