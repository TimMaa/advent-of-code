def apply_rules(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]

    return [stone * 2024]


def merge_dicts(a, b):
    for k, v in b.items():
        a[k] = a[k] + v if k in a.keys() else v
    return a


def update_dict(stone_dict, stone_list):
    for s in stone_list:
        stone_dict[s] = stone_dict[s] + 1 if s in stone_dict.keys() else 1
    return stone_dict


with open("./input.txt", "r") as input:
    for line in input:
        stones = list(map(int, line.strip().split()))
        stone_count = update_dict({}, stones)

        for i in range(0, 75):
            new_dict = {}

            for s in stone_count.keys():
                new_stones = apply_rules(s)
                temp_dict = update_dict({}, new_stones)

                for kns, vns in (x for x in temp_dict.items() if s in stone_count.keys()):
                    temp_dict[kns] = stone_count[s] * vns

                merge_dicts(new_dict, temp_dict)

            stone_count = new_dict

            if i == 24 or i == 74:
                print(sum(stone_count.values()))
