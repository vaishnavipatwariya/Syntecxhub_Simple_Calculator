# Simple Command-line Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Divide by zero!"
    return a / b

def calculator():
    print("🧮 Simple Command-line Calculator")
    print("Supports: +  -  *  /")
    print("Type 'clear' to reset or 'exit' to quit.\n")

    while True:
        choice = input("Enter expression (e.g., 5 + 3): ")

        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        elif choice.lower() == 'clear':
            print("Calculator cleared!\n")
            continue

        parts = choice.split()
        if len(parts) != 3:
            print("Invalid format! Use: number operator number\n")
            continue

        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator! Use + - * / only.\n")
                continue

            print("Result:", result, "\n")

        except ValueError:
            print("Invalid numbers! Please enter valid numeric values.\n")

if __name__ == "__main__":
    calculator()
