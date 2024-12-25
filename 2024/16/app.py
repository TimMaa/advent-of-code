directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start_dir = (0, 1)
maze = []
start = None
goal = None


def find_shortest_path(cost, node, dir):
    closed_list = []
    open_list = [(cost, node, dir, [])]

    while len(open_list) > 0:
        open_list.sort()
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        cur_cost, cur_pos, cur_dir, cur_path = current_node

        if cur_pos == goal:
            return current_node, [c[1] for c in closed_list]

        for d in directions:
            next_node = tuple(map(sum, zip(cur_pos, d)))
            if next_node in maze and next_node not in [v[1] for v in closed_list]:
                next_cost = cur_cost + (1 if d == cur_dir else 1001)
                existing_node = next(
                    (o for o in open_list if o[1] == next_node), None)
                if existing_node and next_cost < existing_node[0] and d == existing_node[2]:
                    open_list.remove(existing_node)
                open_list.append(
                    (next_cost, next_node, d, cur_path + [cur_pos]))


x = 0
y = 0

with open("./input.txt", "r") as input:
    for line in input:
        y = 0
        for c in line:
            if c == ".":
                maze.append((x, y))
            elif c == "S":
                maze.append((x, y))
                start = (x, y)
            elif c == "E":
                maze.append((x, y))
                goal = (x, y)
            y += 1
        x += 1

path, tested_nodes = find_shortest_path(0, start, start_dir)

for xc in range(x):
    for yc in range(y):
        if (xc, yc) == start:
            print("\033[96mS\033[0m", end="")
        elif (xc, yc) == goal:
            print("\033[96mE\033[0m", end="")
        elif (xc, yc) in path[3]:
            print('\033[93mX\033[0m', end="")
        elif (xc, yc) in tested_nodes:
            print("\033[91mO\033[0m", end="")
        elif (xc, yc) in maze:
            print(".", end="")
        else:
            print("#", end="")
    print(xc)

# My Answer is off by 12. Why? I don't know. Will need to figure it out another time.
# 9448 too low
print(path[0])
print(len(path[3]))
