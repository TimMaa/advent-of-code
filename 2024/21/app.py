# 113884058020390 too low, 259496877142375 too high

numpad = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0), "5": (1, 1), "6": (
    1, 2), "1": (2, 0), "2": (2, 1), "3": (2, 2), "0": (3, 1), "A": (3, 2)}
numpad_empty = (3, 0)
dirpad = {
    (-1, 0): (0, 1),  # Up
    "A": (0, 2),  # A
    (0, -1): (1, 0),  # Left
    (1, 0): (1, 1),  # Down
    (0, 1): (1, 2),  # Right
}
dirpad_empty = (0, 0)
numpad_start = numpad["A"]
dirpad_start = dirpad["A"]
known_paths = {}


def find_keypad_path(start, end):
    path = []
    dis_x, dis_y = end[0] - start[0], end[1] - start[1]
    if start[0] == 3 and end[0] != 0:
        while dis_x < 0:
            path.append((-1, 0))
            dis_x += 1
        while dis_y > 0:
            path.append((0, 1))
            dis_y -= 1
        while dis_y < 0:
            path.append((0, -1))
            dis_y += 1
    elif start[1] == 0 and end[1] != 3:
        while dis_y > 0:
            path.append((0, 1))
            dis_y -= 1
        while dis_x > 0:
            path.append((1, 0))
            dis_x -= 1
        while dis_x < 0:
            path.append((-1, 0))
            dis_x += 1
    else:
        while dis_x > 0:
            path.append((1, 0))
            dis_x -= 1
        while dis_y > 0:
            path.append((0, 1))
            dis_y -= 1
        while dis_y < 0:
            path.append((0, -1))
            dis_y += 1
        while dis_x < 0:
            path.append((-1, 0))
            dis_x += 1

    path.append("A")
    return path


def find_directionalpad_path(start, end):
    if (start, end) in known_paths:
        return known_paths[(start, end)]
    path = []
    dis_x, dis_y = end[0] - start[0], end[1] - start[1]
    while dis_x < 0:
        path.append((-1, 0))
        dis_x += 1
    while dis_y > 0:
        path.append((0, 1))
        dis_y -= 1
    while dis_y < 0:
        path.append((0, -1))
        dis_y += 1
    while dis_x > 0:
        path.append((1, 0))
        dis_x -= 1
    path.append("A")
    known_paths[(start, end)] = path
    return path


def visualize(path):
    visual = []
    for c in path:
        if c == (1, 0):
            visual.append("v")
        if c == (-1, 0):
            visual.append("^")
        if c == (0, 1):
            visual.append(">")
        if c == (0, -1):
            visual.append("<")
        if c == "A":
            visual.append(c)
    return "".join(visual)


full_complexity = 0
lvl2_complexity = 0
with open("./input.txt", "r") as input:
    for line in input:
        numeric_part = []
        start_loc = numpad_start
        code_path = []
        for c in line.strip():
            if c.isnumeric():
                numeric_part.append(c)
            path = find_keypad_path(start_loc, numpad[c])
            start_loc = numpad[c]
            code_path += path

        number = int("".join(numeric_part))
        last_level = code_path

        for i in range(15):
            start_loc = dirpad_start
            level_path = []
            for code in last_level:
                path = find_directionalpad_path(start_loc, dirpad[code])
                start_loc = dirpad[code]
                level_path += path
            last_level = level_path
            if i == 1:
                lvl2_complexity += number * len(last_level)

        total_steps = len(last_level) * pow(2.474728747, 11)
        full_complexity += number * total_steps
        

        # print("Last Level takes", len(last_level), "steps")
        # print("Numeric Part is", number)
        # print("Complexity is", number * len(last_level))

        # print(visualize(code_path))
        # print(visualize(level1_path))
        # print(visualize(level2_path))

    print(lvl2_complexity)
    print(full_complexity)
