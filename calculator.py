# calculator minimum

try:
    first: float = float(input("First:"))
    Operator: str = input("Operator (+ ,- , * , /) only:")
    second: float = float(input("Second:"))

    if Operator == "+":
        result = first + second
    elif Operator == "-":
        result = first - second
    elif Operator == "*":
        result = first * second
    elif Operator == "/":
        if second == 0:
            print("Cannot divide with zero")
            exit()
        result = first / second
    else:
        print("choose valid Operator")
        exit()

    print(f"Result is {result}")
except ValueError:
    print("Error: Please enter numbers only")
