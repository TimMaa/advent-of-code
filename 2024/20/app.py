directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
track = []
start = None
end = None


def compute_path(current, visited):
    path = {0: current}
    while current != end:
        for dir in directions:
            next_node = tuple(map(sum, zip(current, dir)))
            if next_node in visited:
                continue
            if next_node in track:
                path[len(visited)] = (next_node)
                visited.append(next_node)
                current = next_node
                break
    return path


def find_cheats(path, cheat_length):
    cheats = {}
    for c_val, c_node in path.items():
        for t_val, t_node in path.items():
            distance = abs(c_node[0] - t_node[0]) + abs(c_node[1] - t_node[1])
            time_save = t_val - c_val - distance
            if distance <= cheat_length and time_save > 0:
                if time_save not in cheats.keys():
                    cheats[time_save] = []
                cheats[time_save].append((c_node, t_node))
    return cheats


with open("./input.txt", "r") as input:
    for x, line in enumerate(input):
        for y, c in enumerate(line.strip()):
            if c == "#":
                continue
            track.append((x, y))
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)

path = compute_path(start, [start])

# Part 1
print(sum((len(v) for k, v in find_cheats(path, 2).items() if k > 99)))
# Part 2
print(sum((len(v) for k, v in find_cheats(path, 20).items() if k > 99)))
