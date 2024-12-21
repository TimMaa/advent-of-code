# got 190248267039386 should be 118392478819140

numpad = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0), "5": (1, 1), "6": (
    1, 2), "1": (2, 0), "2": (2, 1), "3": (2, 2), "0": (3, 1), "A": (3, 2)}
dirpad = {
    (-1, 0): (0, 1),  # Up
    "A": (0, 2),  # A
    (0, -1): (1, 0),  # Left
    (1, 0): (1, 1),  # Down
    (0, 1): (1, 2),  # Right
}


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
    path = []
    dis_x, dis_y = end[0] - start[0], end[1] - start[1]
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


full_complexity = 0
lvl2_complexity = 0

with open("./input.txt", "r") as input:
    for line in input:
        numeric_part = []
        start_loc = (3, 2)  # numpad["A"]
        code_instructions = {}
        for c in line.strip():
            if c.isnumeric():
                numeric_part.append(c)

            path = tuple(find_keypad_path(start_loc, numpad[c]))
            if path in code_instructions.keys():
                code_instructions[path] += 1
            else:
                code_instructions[path] = 1
            start_loc = numpad[c]

        number = int("".join(numeric_part))
        last_level = code_instructions

        for k in range(26):
            start_loc = (0, 2)  # dirpad["A"]
            level_path = {}
            for inst, val in last_level.items():
                inst_path = []
                for i in inst:
                    path = find_directionalpad_path(start_loc, dirpad[i])
                    inst_path.append(path)
                    start_loc = dirpad[i]
                    tp = tuple(path)
                    if tp in level_path.keys():
                        level_path[tp] += val
                    else:
                        level_path[tp] = val
            last_level = level_path

            if k == 2:
                lvl2_complexity += number * sum(last_level.values())
            if k == 25:
                full_complexity += number * sum(last_level.values())

    print(lvl2_complexity)
    print(full_complexity)
