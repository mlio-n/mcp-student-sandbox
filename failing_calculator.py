def average_ratios(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")

    non_zero_numbers = [number for number in numbers if number != 0]
    if not non_zero_numbers:
        raise ValueError("numbers must contain at least one non-zero value")

    total = 0
    for number in non_zero_numbers:
        total += 100 / number
    return total / len(non_zero_numbers)


if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))
