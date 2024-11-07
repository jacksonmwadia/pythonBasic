# Get input from user
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

#  calculation based on the operation entered
if operation == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero")
    else:
        result = num1 / num2
        print(f"The result is: {result}")
else:
    print("Invalid cross check the input")
