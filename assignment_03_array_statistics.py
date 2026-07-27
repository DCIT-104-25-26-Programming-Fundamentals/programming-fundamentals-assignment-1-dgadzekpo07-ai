def calculate_sum(numbers):
    """Return the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    """Return the maximum value in the list (no built-in max())."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_min(numbers):
    """Return the minimum value in the list (no built-in min())."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)

    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()