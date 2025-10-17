import math

def calculator():
    print("=== Advanced Calculator ===")
    print("Available operations: +, -, *, /, %, ^, sin, cos, tan, log, sqrt, exit")

    while True:
        op = input("\nEnter operation: ").lower()

        if op == "exit":
            print("Goodbye 👋")
            break

        try:
            if op in ["sin", "cos", "tan", "log", "sqrt"]:
                x = float(input("Enter value: "))
                if op == "sin": print("Result =", math.sin(math.radians(x)))
                elif op == "cos": print("Result =", math.cos(math.radians(x)))
                elif op == "tan": print("Result =", math.tan(math.radians(x)))
                elif op == "log": print("Result =", math.log10(x))
                elif op == "sqrt": print("Result =", math.sqrt(x))
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if op == "+": print("Result =", a + b)
                elif op == "-": print("Result =", a - b)
                elif op == "*": print("Result =", a * b)
                elif op == "/": print("Result =", a / b)
                elif op == "%": print("Result =", a % b)
                elif op == "^": print("Result =", math.pow(a, b))
                else: print("Invalid operation!")
        except Exception as e:
            print("Error:", e)

calculator()