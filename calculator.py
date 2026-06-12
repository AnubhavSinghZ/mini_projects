print("--- My First Python Calculator by Me ---")
active = True

while active:
    print("\nOptions: +, -, *, /, or 'exit' to quit")
    user_input = input("Choose an operation: ").lower()
    if user_input == "exit":
        active = False
    elif user_input in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "+": print(f"Result: {num1 + num2}")
        elif user_input == "-": print(f"Result: {num1 - num2}")
        elif user_input == "*": print(f"Result: {num1 * num2}")
        elif user_input == "/": print(f"Result: {num1 / num2}")
    else:
        print("Invalid! Try Again")