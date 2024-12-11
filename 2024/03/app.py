import re

# One-Liner for Part 1
print(sum([sum(
    [int(a)*int(b) for a, b in re.findall("mul\((\d{1,3})\,(\d{1,3})\)", l)])
    for l in open("./input.txt", "r")])
)

# Combined with Part 1
with open("./input.txt", "r") as input:
    enabled = True
    sum = 0
    cond_sum = 0
    for line in input:
        instructions = re.findall(
            "mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don't\(\))", line)
        for a, b, y, n in instructions:
            if a and b:
                sum += int(a) * int(b)
            if y:
                enabled = True
            elif n:
                enabled = False
            elif enabled == True:
                cond_sum += int(a) * int(b)
    print(sum)
    print(cond_sum)
