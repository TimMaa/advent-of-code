directions = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
]

perpendiculars = {
    (0, 1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, 1), (0, -1)],
    (0, -1): [(1, 0), (-1, 0)],
    (1, 0): [(0, 1), (0, -1)]
}

garden = {}
regions = []


def calc_perimeter(region: list[tuple[int, int]]):
    perimeter = 0
    for p in region:
        for _ in (True for dir in directions if tuple(map(sum, zip(p, dir))) not in region):
            perimeter += 1

    return perimeter


def calc_sides(region: list[tuple[int, int]]):
    sides = {d: [] for d in directions}
    for coord in region:
        for d in directions:
            if not any(coord in s for s in sides[d]) and tuple(map(sum, zip(coord, d))) not in region:
                full_side = [coord]
                for p in perpendiculars[d]:
                    next_coord = tuple(map(sum, zip(coord, p)))
                    while next_coord in region and tuple(map(sum, zip(next_coord, d))) not in region:
                        full_side.append(next_coord)
                        next_coord = tuple(map(sum, zip(next_coord, p)))
                sides[d].append(full_side)
    return sum(len(side) for side in sides.values())


def expand_region(coords: list[tuple[int, int]], p: str) -> list[tuple[int, int]]:
    found_more = False
    for coord in coords:
        if any(coord in r for r in regions):
            return []

        for d in directions:
            n_coord = tuple(map(sum, zip(coord, d)))
            if n_coord not in coords and n_coord in garden.keys() and garden[n_coord] == p:
                coords.append(n_coord)
                found_more = True
    return expand_region(coords, p) if found_more else coords


with open("./input.txt", "r") as input:
    for r_idx, line in enumerate(input):
        for c_idx, p in enumerate(line.strip()):
            garden[(r_idx, c_idx)] = p


for coord, p in garden.items():
    result = expand_region([coord], p)
    if len(result) > 0:
        regions.append(result)

print(sum(len(r) * calc_perimeter(r) for r in regions))
print(sum(len(r) * calc_sides(r) for r in regions))
