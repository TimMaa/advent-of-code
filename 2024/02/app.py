basic_safe = 0
dampened_safe = 0


def isSafe(record):
    return True if (
        all(record[i] - record[i+1] < 4 and record[i] - record[i+1] > 0
            for i in range(len(record) - 1)) or
        all(record[i] - record[i+1] > -4 and record[i] - record[i+1] < 0
            for i in range(len(record) - 1))
    ) else False


with open("./input.txt", "r") as input:
    for line in input:
        record = list(map(int, line.split()))
        if isSafe(record):
            basic_safe += 1
            dampened_safe += 1
        else:
            for i in range(len(record)):
                if isSafe(record[0:i] + record[i+1:len(record)]):
                    dampened_safe += 1
                    break

print(basic_safe)
print(dampened_safe)
