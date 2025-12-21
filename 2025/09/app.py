red_tiles = []
green_tiles = []
largest_area = 0

with open("./input.txt", "r") as input:
    for line in input:
        next_tile = tuple(map(int, line.rstrip().split(",")))
        red_tiles.append(next_tile)

    largest_area = max([abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
                       for x1, y1 in red_tiles for x2, y2 in red_tiles])
    print("Part 1:", largest_area)
