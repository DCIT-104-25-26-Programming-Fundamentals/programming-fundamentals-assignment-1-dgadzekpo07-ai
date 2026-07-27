# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
# =============================================================================


def generate_fibonacci(n):
    """Return a list of the first n Fibonacci numbers, using a loop."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_first_n_terms():
    """Part A: ask for N and print the first N Fibonacci terms."""
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci(n)
    terms = " ".join(str(term) for term in sequence)
    print(f"Fibonacci sequence: {terms}")


def is_fibonacci_number(number):
    """Part B helper: return True if number appears in the Fibonacci sequence."""
    if number < 0:
        return False

    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b
    return False


def check_number():
    """Part B: ask for a number and report whether it's a Fibonacci number."""
    number = int(input("Enter a number to check: "))

    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    print("--- Part A: First N Terms ---")
    print_first_n_terms()

    print("\n--- Part B: Check if a Number Belongs to the Sequence ---")
    check_number()


if __name__ == "__main__":
    main()