# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
# =============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b rounded to 2 decimal places, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def print_menu():
    """Display the main menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_two_numbers():
    """Prompt for two numbers, returning None if input is invalid."""
    try:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: please enter valid numbers.")
        return None


def format_number(value):
    """Display whole-number results without a trailing .0."""
    if value == int(value):
        return str(int(value))
    return str(value)


def main():
    symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "%",
        "6": "**",
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in symbols:
            print("Error: please enter a number from 1 to 7.")
            print()
            continue

        numbers = get_two_numbers()
        if numbers is None:
            print()
            continue
        a, b = numbers

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "5":
            result = modulus(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "6":
            result = exponentiate(a, b)

        symbol = symbols[choice]
        print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")
        print()


if __name__ == "__main__":
    main()