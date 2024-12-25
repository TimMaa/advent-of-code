locks = []
keys = []
with open("./input.txt", "r") as input:
    i = 0
    current = []
    for line in input:
        if line.strip() == "":
            i = 0
            continue
        if i == 0:
            current = [0 for _ in range(len(line))]
            i += 1
            continue
        elif i == 6:
            if "." in line.strip():
                locks.append(current)
            else:
                keys.append(current)
        else:
            row = [0 if c == "." else 1 for c in line.strip()]
            current = [c+r for c, r in zip(current, row)]

        i += 1

total = 0
for key in keys:
    for lock in locks:
        if all((v < 6 for v in [k+l for k, l in zip(key, lock)])):
            total += 1
print(total)
