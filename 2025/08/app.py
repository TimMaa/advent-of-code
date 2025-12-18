boxes = {}
distances = {}
cables = 10
circuits = []


def calculate_distance(box1, box2):
    return (abs(box1[0] - box2[0]) ** 2 + abs(box1[1] - box2[1]) ** 2 + abs(box1[2] - box2[2]) ** 2) ** 0.5


with open("./input.txt", "r") as input:
    for idx, line in enumerate(input):
        boxes[idx] = tuple(map(int, line.rstrip().split(",")))

    for id1, box1 in boxes.items():
        for id2, box2 in boxes.items():
            if id1 == id2:
                continue
            else:
                distances[(min(id1, id2), max(id1, id2)
                           )] = calculate_distance(box1, box2)

    s_distances = sorted(distances.items(), key=lambda x: x[1])

    for _ in range(cables):
        closest = s_distances.pop(0)[0]
        matches = list(
            filter(lambda c: closest[0] in c or closest[1] in c, circuits))
        for m in matches:
            circuits.remove(m)
        circuits.append(set(closest).union(*matches))

    sc = [len(c) for c in sorted(
        circuits, key=lambda c: len(c), reverse=True)[:3]]
    print("Part 1:", sc[0] * sc[1] * sc[2])

    while len(circuits[0]) != len(boxes):
        closest = s_distances.pop(0)[0]
        matches = list(
            filter(lambda c: closest[0] in c or closest[1] in c, circuits))
        for m in matches:
            circuits.remove(m)
        circuits.append(set(closest).union(*matches))

    print("Part 2:", boxes[closest[0]][0] * boxes[closest[1]][0])
