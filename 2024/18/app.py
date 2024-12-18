size = 71  # 71 for real, 7 in example
blocks = []
start = (0, 0)
end = (size-1, size-1)
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def find_shortest_path(cost, node):
    closed_list = []
    open_list = [(cost, node, [])]

    while len(open_list) > 0:
        open_list.sort(reverse=True)
        current_node = open_list.pop()
        closed_list.append(current_node)

        if current_node[1] == end:
            return current_node

        for d in directions:
            next_node = tuple(map(sum, zip(current_node[1], d)))
            if next_node[0] in range(0, size) and next_node[1] in range(0, size) and next_node not in blocks and next_node not in [v[1] for v in closed_list]:
                next_cost = current_node[0] + 1
                try:
                    existing_node = next(
                        o for o in open_list if o[1] == next_node)
                    if next_cost < existing_node[0]:
                        open_list.remove(existing_node)
                        open_list.append(
                            (next_cost, next_node, current_node[2] + [current_node[1]]))
                except StopIteration:
                    open_list.append(
                        (next_cost, next_node, current_node[2] + [current_node[1]]))


prev_path = None
with open("./input.txt", "r") as input:
    for i, line in enumerate(input):
        blocks.append(tuple(map(int, line.strip().split(","))))
        if i > 1023:
            if blocks[-1] in prev_path:
                path = find_shortest_path(0, start)
                if path == None:
                    print(blocks[-1])
                    break
                else:
                    prev_path = path[2]
        elif i == 1023:
            path = find_shortest_path(0, start)
            print(path[0])
            prev_path = path[2]
