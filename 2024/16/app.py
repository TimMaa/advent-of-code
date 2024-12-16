directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
start_dir = (0, 1)
maze = []
start = None
end = None


def find_shortest_path(cost, node, dir):
    closed_list = []
    open_list = [(cost, node, dir, [])]
    possible_paths = []

    while len(open_list) > 0:
        open_list.sort(reverse=True)
        current_node = open_list.pop()
        closed_list.append(current_node)

        if current_node[1] == end:
            possible_paths.append(current_node)
            continue

        for d in directions:
            next_node = tuple(map(sum, zip(current_node[1], d)))
            if next_node in maze and next_node not in [v[1] for v in closed_list]:
                next_cost = current_node[0] + \
                    (1 if d == current_node[2] else 1001)
                try:
                    existing_node = next(
                        o for o in open_list if o[1] == next_node)
                    if next_cost < existing_node[0]:
                        open_list.remove(existing_node)
                        open_list.append(
                            (next_cost, next_node, d, current_node[3] + [current_node[1]]))
                except StopIteration:
                    open_list.append(
                        (next_cost, next_node, d, current_node[3] + [current_node[1]]))

    return sorted(possible_paths)[0]


with open("./input.txt", "r") as input:
    for x, line in enumerate(input):
        for y, c in enumerate(line):
            if c == ".":
                maze.append((x, y))
            elif c == "S":
                start = (x, y)
            elif c == "E":
                maze.append((x, y))
                end = (x, y)

path = find_shortest_path(0, start, start_dir)

# My Answer is off by 12. Why? I don't know. Will need to figure it out another time.
print(path[0])
print(len(path[3]))
