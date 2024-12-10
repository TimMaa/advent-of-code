directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
best_trail = [x for x in range(0, 10)]

topography = []


def find_trail(spot, idx):
    if spot[0] not in range(0, len(topography)) or spot[1] not in range(0, len(topography[spot[0]])):
        return None

    if topography[spot[0]][spot[1]] == best_trail[idx]:
        if idx == len(best_trail) - 1:
            return [spot]

        trails = [find_trail(tuple(map(sum, zip(spot, dir))), idx+1)
                  for dir in directions]
        return list(t for trail in trails if trail for t in trail)

    return None


with open("./input.txt", "r") as input:
    for line in input:
        topography.append([int(x) for x in line.strip()])

    total_score = 0
    total_rating = 0

    for r_idx in range(0, len(topography)):
        for c_idx in range(0, len(topography[r_idx])):
            trails = find_trail((r_idx, c_idx), 0)
            if trails:
                total_score += len(set(trails))
                total_rating += len(trails)

print(total_score)
print(total_rating)
