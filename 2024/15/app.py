directions = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}

walls_p1 = []
boxes_p1 = []
robot_p1 = None

walls_p2 = []
boxes_p2 = []
robot_p2 = None


def move(pos, dir):
    new_pos = tuple(map(sum, zip(pos, dir)))
    if new_pos in walls_p1:
        return pos

    if new_pos in boxes_p1:
        box_target = move(new_pos, dir)
        if box_target != new_pos:
            boxes_p1.remove(new_pos)
            boxes_p1.append(box_target)
            return new_pos
        else:
            return pos
    else:
        return new_pos


def move_big(pos, dir):
    new_pos = tuple(map(sum, zip(pos, dir)))

    if new_pos in walls_p2:
        # print("WALL AT", new_pos)
        return pos

    box = next((box for box in boxes_p2 if new_pos in box), None)

    if box != None:
        # print("FOUND BOX", box, "IN DIR", dir)
        if dir == (0, -1):
            # print("MOVE LEFT")
            box_target = move_big(box[0], dir)
            if box_target != box[0]:
                boxes_p2.remove(box)
                boxes_p2.append([box_target, box[0]])
                return new_pos
            else:
                return pos
        elif dir == (0, 1):
            # print("MOVE RIGHT")
            box_target = move_big(box[1], dir)
            if box_target != box[1]:
                boxes_p2.remove(box)
                boxes_p2.append([box[1], box_target])
                return new_pos
            else:
                return pos
        else:
            # print("MOVE UP OR DOWN")
            new_b0_pos = tuple(map(sum, zip(box[0], dir)))
            new_b1_pos = tuple(map(sum, zip(box[1], dir)))
            if new_b0_pos in walls_p2 or new_b1_pos in walls_p2:
                return pos

            b0_target = move_big(box[0], dir)
            b1_target = move_big(box[1], dir)
            if b0_target != box[0] and b1_target != box[1]:
                boxes_p2.remove(box)
                boxes_p2.append([b0_target, b1_target])
                return new_pos
            else:
                return pos
    else:
        return new_pos


with open("./input.txt", "r") as input:
    for x, line in enumerate(input):
        line = line.strip()
        i = 0
        for y, c in enumerate(line):
            if c == "#":
                walls_p1.append((x, y))
                walls_p2.append((x, i))
                walls_p2.append((x, i+1))
                i += 2
            elif c == "O":
                boxes_p1.append((x, y))
                boxes_p2.append([(x, i), (x, i+1)])
                i += 2
            elif c == "@":
                robot_p1 = (x, y)
                robot_p2 = (x, i)
                i += 2
            elif c == ".":
                i += 2
            else:
                robot_p1 = move(robot_p1, directions[c])
                robot_p2 = move_big(robot_p2, directions[c])

print(sum([100*x+y for x, y in boxes_p1]))
print(sum([100*x+y for x, y in [b for b, _ in boxes_p2]]))
