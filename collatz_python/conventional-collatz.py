import time


def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def longest_sequence_in_range(range_limit):
    longest_sequence = []
    number_with_longest_sequence = 0

    # range limit + 1 because range() stops before the limit
    for i in range(1, range_limit + 1):
        current_sequence = collatz_sequence(i)
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
            number_with_longest_sequence = i

    return number_with_longest_sequence, longest_sequence


def main():
    starting_number_limit = int(input("Enter number up to which sequence is to be calculated: "))

    start_time = time.time()
    number, sequence = longest_sequence_in_range(starting_number_limit)
    end_time = time.time()

    duration = end_time - start_time

    print(f"The number between 1 and {starting_number_limit} that produces the longest Collatz sequence is {number} "
          f"and has {len(sequence)} elements.")
    print(f"The sequence is: {sequence}")
    print(f"It took {duration} seconds to calculate.")


main()
