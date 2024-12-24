gates = {}
operations = []

validated_zs = []


with open("./input.txt", "r") as input:
    for line in input:
        if ":" in line:
            w, v = line.strip().split(":")
            gates[w] = int(v)
        if "->" in line:
            w1, op, w2, _, t = line.strip().split(" ")
            operations.append((w1, w2, op, t))

i = 0
while i < len(operations):
    op = operations[i]
    if op[0] in gates.keys() and op[1] in gates.keys():
        if op[2] == "AND":
            gates[op[3]] = gates[op[0]] & gates[op[1]]
        elif op[2] == "OR":
            gates[op[3]] = gates[op[0]] | gates[op[1]]
        elif op[2] == "XOR":
            gates[op[3]] = gates[op[0]] ^ gates[op[1]]
        i += 1
    else:
        operations.append(operations.pop(i))

actual_z = "".join([str(v) for k, v in sorted(
    gates.items(), reverse=True) if k.startswith("z")])

print(int(actual_z, 2))
