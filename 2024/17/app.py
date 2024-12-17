a, b, c = None, None, None
instructions = []


def interpret_combo(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    if operand == 7:
        return None


with open("./input.txt", "r") as input:
    for line in input:
        name, *values = line.strip().split(" ")
        if name == "Register":
            if values[0] == "A:":
                a = int(values[1])
            elif values[0] == "B:":
                b = int(values[1])
            elif values[0] == "C:":
                c = int(values[1])
        elif name == "Program:":
            instructions = [int(x) for x in values[0].split(",")]

pointer = 0
output = []

while pointer < len(instructions):
    opcode = instructions[pointer]
    lit = instructions[pointer+1]
    comb = interpret_combo(lit)

    if opcode == 0:
        a = a // pow(2, comb)
    elif opcode == 1:
        b = b ^ lit
    elif opcode == 2:
        b = comb % 8
    elif opcode == 3 and a != 0:
        pointer = lit
        continue
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        output.append(str(comb % 8))
    elif opcode == 6:
        b = a // pow(2, comb)
    elif opcode == 7:
        c = a // pow(2, comb)
    pointer += 2

print(",".join(output))
