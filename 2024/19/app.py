def match_pattern(line, patterns, failed_patterns):
    if line in failed_patterns:
        return failed_patterns

    if len(line) == 0:
        return []

    possible_patterns = [p for p in patterns if len(
        p) <= len(line) and p.startswith(line[0:len(p)])]

    if len(possible_patterns) == 0:
        failed_patterns.add(line)

    # print(line, possible_patterns)
    for p in possible_patterns:
        result = match_pattern(line[len(p):], patterns, failed_patterns)
        if len(result) == 0:
            return []
        else:
            failed_patterns.add(line)

    return failed_patterns


with open("./input.txt", "r") as input:
    patterns = [p.strip() for p in input.readline().split(",")]

    input.readline()  # Skip empty line
    possible = 0
    for line in input:
        result = match_pattern(line.strip(), patterns, set())
        if len(result) == 0:
            possible += 1
    print(possible)
