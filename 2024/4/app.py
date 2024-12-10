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

array = []


def search_word(match_word, dir, spot, w_idx):
    if spot[0] not in range(0, len(array)) or spot[1] not in range(0, len(array[spot[0]])):
        return False

    if array[spot[0]][spot[1]] != match_word[w_idx]:
        return False

    if w_idx == len(match_word) - 1:
        return True

    return search_word(match_word, dir, tuple(map(sum, zip(spot, dir))), w_idx+1)


with open("./input.txt", "r") as input:
    for line in input:
        array.append([l for l in line.strip()])

    cnt = 0
    x_cnt = 0

    for l_idx in range(0, len(array)):
        for c_idx in range(0, len(array[l_idx])):
            for dir in directions:
                if search_word("XMAS", dir, (l_idx, c_idx), 0):
                    cnt += 1
                if search_word("MAS", dir, (l_idx, c_idx), 0):
                    x_dir = x_params[dir]
                    new_spot = tuple(
                        map(sum, zip((l_idx, c_idx), x_dir[1])))
                    if search_word("MAS", x_dir[0], new_spot, 0):
                        x_cnt += 1

    print(cnt)
    # Answer is 31 too high, should be 1871. Am I double counting somewhere?
    print(x_cnt)
