# WAP to create a simple calculator that can perform addition, subtraction, multiplication, and division based on user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "1":
    result = num1 + num2
    print("Result =", result)

elif operator == "2":
    result = num1 - num2
    print("Result =", result)

elif operator == "3":
    result = num1 * num2
    print("Result =", result)

elif operator == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")