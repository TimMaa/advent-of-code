directions = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}

walls = []
boxes = []
robot = None


def move(pos, dir):
    new_pos = tuple(map(sum, zip(pos, dir)))
    if new_pos in walls:
        return pos
    elif new_pos in boxes:
        box_target = move(new_pos, dir)
        if box_target != new_pos:
            boxes.remove(new_pos)
            boxes.append(box_target)
            return new_pos
        else:
            return pos
    else:
        return new_pos


with open("./input.txt", "r") as input:
    for x, line in enumerate(input):
        for y, c in enumerate(line.strip()):
            if c == "#":
                walls.append((x, y))
            elif c == "O":
                boxes.append((x, y))
            elif c == "@":
                robot = (x, y)
            elif c == ".":
                continue
            else:
                robot = move(robot, directions[c])

print(sum([100*x+y for x, y in boxes]))
