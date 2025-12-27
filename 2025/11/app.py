connections = {}
start_1 = "you"
target = "out"
working_paths_1 = 0

with open("./input.txt", "r") as input:
    for line in input:
        start, targets = line.split(":")
        connections[start] = targets.strip().split(" ")

    paths = [[start_1]]
    while paths:
        path = [*paths.pop(0)]
        for output in connections[path[-1]]:
            if output == target:
                working_paths_1 += 1
                continue
            paths.append([*path, output])

    print("Part 1:", working_paths_1)
