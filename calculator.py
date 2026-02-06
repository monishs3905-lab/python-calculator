a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
symbol = input("Choose operation (+, -, *, /): ")

if symbol == "+":
    print("Result:", a + b)
elif symbol == "-":
    print("Result:", a - b)
elif symbol == "*":
    print("Result:", a * b)
elif symbol == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator")
