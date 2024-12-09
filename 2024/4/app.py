directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
]

x_params = {
    (0, 1): [(1, 0), (-1, 1)],
    (1, 1): [(1, -1), (0, 2)],
    (1, 0): [(0, -1), (1, 1)],
    (1, -1): [(-1, -1), (2, 0)],
    (0, -1): [(-1, 0), (1, -1)],
    (-1, -1): [(-1, 1), (0, -2)],
    (-1, 0): [(0, 1), (-1, -1)],
    (-1, 1): [(1, 1), (-2, 0)],
}


def search_word(match_word, arr, dir, start, w_idx):
    if w_idx == len(match_word):
        return True

    new_l, new_c = map(sum, zip(start, dir))

    return search_word(match_word, arr, dir, (new_l, new_c), w_idx+1) if new_l in range(0, len(arr)) and new_c in range(0, len(arr[0])) and arr[new_l][new_c] == match_word[w_idx] else False


with open("./input.txt", "r") as input:
    array = []
    for line in input:
        array.append([l for l in line.strip()])

    cnt = 0
    x_cnt = 0

    for l_idx, line in enumerate(array):
        for c_idx, char in enumerate(line):
            if char == "X":
                for dir in directions:
                    if search_word("XMAS", array, dir, (l_idx, c_idx), 1):
                        cnt += 1
            if char == "M":
                for dir in directions:
                    if search_word("MAS", array, dir, (l_idx, c_idx), 1):
                        x_param = x_params[dir]
                        new_l, new_c = tuple(
                            map(sum, zip((l_idx, c_idx), x_param[1])))
                        if new_l in range(0, len(array)) and new_c in range(0, len(array[0])) and array[new_l][new_c] == "M":
                            if search_word("MAS", array, x_param[0], (new_l, new_c), 1):
                                x_cnt += 1

    print(cnt)
    print(x_cnt)
