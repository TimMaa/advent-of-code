joltage_1 = 0
joltage_2 = 0


def find_biggest_number(digits: str, end: int):
    digit = str(max([int(j) for j in digits[0:]])) if end == 1 else str(
        max([int(j) for j in digits[0:-end+1]]))
    next_digits = []
    if (end > 1):
        next_digits = find_biggest_number(
            digits[digits.index(digit)+1:], end-1)
    return [digit] + next_digits


with open("./input.txt", "r") as input:
    for line in input:
        joltage_1 += int("".join(find_biggest_number(line.rstrip(), 2)))
        joltage_2 += int("".join(find_biggest_number(line.rstrip(), 12)))
    print(joltage_1)
    print(joltage_2)
