mode = 0
fresh_map = []
fresh_count = 0
total_count = 0


def reduce_ranges(range_list: list):
    range_list.sort(key=lambda x: x[0])
    reduced_list = []
    r = range_list.pop(0)
    while len(range_list):
        s = range_list.pop(0)
        if r[1] >= s[0]:
            if r[1] >= s[1]:
                continue
            else:
                r = (r[0], s[1])
        else:
            reduced_list.append(r)
            r = s
    reduced_list.append(r)
    return reduced_list


with open("./input.txt", "r") as input:
    for line in input:
        val = line.rstrip()
        if not val:
            mode = 1
            new_ranges = reduce_ranges(fresh_map)
            for r in new_ranges:
                total_count += r[1] - r[0] + 1
            print("Part 2:", total_count)
            continue
        if mode == 0:
            start, end = map(int, val.split("-"))
            fresh_map.append((start, end))
        elif mode == 1:
            for r in new_ranges:
                if int(val) >= r[0] and int(val) <= r[1]:
                    fresh_count += 1
                    break

    print("Part 1:", fresh_count)
