base_a, base_b, base_c = None, None, None
instructions = []


def interpret_combo(operand, a, b, c):
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


def run_program(a):
    b = 0
    c = 0
    pointer = 0

    output = []

    while pointer < len(instructions):
        opcode = instructions[pointer]
        literal = instructions[pointer+1]
        combo = interpret_combo(literal, a, b, c)
        if opcode == 0:
            a = a // pow(2, combo)
        elif opcode == 1:
            b = b ^ literal
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3 and a != 0:
            pointer = literal
            continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(str(combo % 8))
        elif opcode == 6:
            b = a // pow(2, combo)
        elif opcode == 7:
            c = a // pow(2, combo)
        pointer += 2
    return output


with open("./input.txt", "r") as input:
    for line in input:
        name, *values = line.strip().split(" ")
        if name == "Register":
            if values[0] == "A:":
                base_a = int(values[1])
            elif values[0] == "B:":
                base_b = int(values[1])
            elif values[0] == "C:":
                base_c = int(values[1])
        elif name == "Program:":
            instructions = [int(x) for x in values[0].split(",")]

print(",".join(run_program(base_a)))

str_inst = list(map(str, instructions))
base_a = pow(8, len(instructions)-1)

while base_a < pow(8, len(instructions))-1:
    base_a += 1
    result = run_program(base_a)
    print(base_a, ";", result)
    if result == str_inst:
        print("Found:", base_a)
        break
