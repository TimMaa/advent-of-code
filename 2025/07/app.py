positions = {}
split_map = []
splits = 0

with open("./input.txt", "r") as input:
    for line in input:
        if not len(positions):
            s = line.find("S")
            positions[s] = 1
            continue

        splitters = [idx for idx, c in enumerate(line) if c == "^"]
        if len(splitters):
            split_map.append(splitters)

    for idx, s in enumerate(split_map):
        new_positions = {}
        for p, c in positions.items():
            if p in s:
                splits += 1
                if p+1 in new_positions:
                    new_positions[p+1] += c
                else:
                    new_positions[p+1] = c
                if p-1 in new_positions:
                    new_positions[p-1] += c
                else:
                    new_positions[p-1] = c
            else:
                if p in new_positions:
                    new_positions[p] += c
                else:
                    new_positions[p] = c
        positions = new_positions

    print("Part 1:", splits)
    print("Part 2:", sum(positions.values()))
