# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# =============================================================================


def print_table(number):
    """Print the multiplication table for a single number, 1 through 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        product = number * i
        print(f"{number}  x  {i:<2} =  {product}")


def print_tables_up_to_n(n):
    """Part B: print full multiplication tables for every number 1..n."""
    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("-" * 29)


def part_a():
    """Ask for a number and print its multiplication table."""
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    print_table(number)


def part_b():
    """Ask for N and print tables for every number from 1 to N."""
    try:
        n = int(input("Enter N: "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_up_to_n(n)


def main():
    print("--- Part A: Single Table ---")
    part_a()

    print("\n--- Part B: Tables from 1 to N ---")
    part_b()


if __name__ == "__main__":
    main()