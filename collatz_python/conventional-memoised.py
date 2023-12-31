import time


# only runs once when we know for sure which number produces the longest sequence
def collatz_sequence(number_of_longest_sequence):
    sequence = [number_of_longest_sequence]
    while number_of_longest_sequence != 1:
        if number_of_longest_sequence % 2 == 0:
            number_of_longest_sequence = number_of_longest_sequence // 2
        else:
            number_of_longest_sequence = 3 * number_of_longest_sequence + 1
        sequence.append(number_of_longest_sequence)
    return sequence


def collatz_sequence_length_memorised(number, memory):
    if number in memory:
        return memory[number]

    # copy of number because the original number changes during calculation
    original_number = number
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        if number in memory:
            memory[original_number] = memory[number] + length
            return memory[original_number]

        length += 1

    memory[original_number] = length
    return length


def longest_sequence_in_range(range_limit):
    longest_length = 0
    number_with_longest_sequence = 0
    sequence_dict = {}

    for i in range(1, range_limit + 1):
        current_length = collatz_sequence_length_memorised(i, sequence_dict)
        if current_length > longest_length:
            longest_length = current_length
            number_with_longest_sequence = i

    longest_sequence = collatz_sequence(number_with_longest_sequence)

    return number_with_longest_sequence, longest_length, longest_sequence


def main():
    starting_number_limit = int(input("Enter number up to which sequence is to be calculated: "))

    start_time = time.time()
    number, length, sequence = longest_sequence_in_range(starting_number_limit)
    end_time = time.time()

    duration = end_time - start_time

    print(f"The number between 1 and {starting_number_limit} that produces the longest Collatz sequence is {number} "
          f"and has {length} elements.")
    print(f"The elements are: {sequence}")
    print(f"It took {duration} seconds to calculate.")


main()
