current = 50
count = 0

with open("./input.txt", "r") as input:
    for line in input:
        val = int(line.strip()[1:])
        current += val if line[0] == "R" else -val
        if current % 100 == 0:
            count += 1
    print("Part 1:", count)

current = 50
count = 0

with open("./input.txt", "r") as input:
    for line in input:
        dir = line[0]
        val = int(line.strip()[1:])
        if dir == "R":
            count += (val + (current % 100)) // 100
        if dir == "L":
            count += (val + current % 100) // 100
            if current == 0:
                count -= 1
        current += val if dir == "R" else -val
        if current % 100 == 0:
            count += 1
    print("Part 2:", count)
