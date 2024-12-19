patterns = []
known_patterns = {'': 1}


def match_pattern(design: str):
    if design in known_patterns:
        return known_patterns[design]

    ways = sum(match_pattern(design[len(p):])
               for p in patterns if design.startswith(p))
    known_patterns[design] = ways
    return ways


with open("./input.txt", "r") as input:
    patterns = [p.strip() for p in input.readline().split(",")]

    input.readline()  # Skip empty line

    possible = 0
    variations = 0
    for line in input:
        success = match_pattern(line.strip())
        if success != 0:
            possible += 1
        variations += success

    print(possible)
    print(variations)
