def searchWord(match_word, arr, dir, l, c, w_idx):
    if w_idx == len(match_word):
        return True

    # right
    if dir == 0 and c != len(arr[0]) - 1:
        c += 1
    # right down
    elif dir == 1 and c != len(arr[0]) - 1 and l != len(arr) - 1:
        c += 1
        l += 1
    # down
    elif dir == 2 and l != len(arr) - 1:
        l += 1
    # left down
    elif dir == 3 and c != 0 and l != len(arr) - 1:
        c -= 1
        l += 1
    # left
    elif dir == 4 and c != 0:
        c -= 1
    # left up
    elif dir == 5 and c != 0 and l != 0:
        c -= 1
        l -= 1
    # up
    elif dir == 6 and l != 0:
        l -= 1
    # right up
    elif dir == 7 and c != len(arr[0]) - 1 and l != 0:
        c += 1
        l -= 1

    if c > -1 and l > -1 and arr[l][c] == match_word[w_idx]:
        return searchWord(match_word, arr, dir, l, c, w_idx+1)
    else:
        return False


def searchX(match_word, arr, dir, l, c):
    ls, le, cs, ce = None, None, None, None

    # right
    if dir == 0:
        ls, le = l-1, l+1
        cs, ce = c+1, c+1
    # right down
    elif dir == 1:
        ls, le = l, l-2
        cs, ce = c+2, c
    # down
    elif dir == 2:
        ls, le = l+1, l+1
        cs, ce = c+1, c-1
    # left down
    elif dir == 3:
        ls, le = l-2, l
        cs, ce = c, c-2
    # left
    elif dir == 4:
        ls, le = l+1, l-1
        cs, ce = c-1, c-1
    # left up
    elif dir == 5:
        ls, le = l, l-2
        cs, ce = c-2, c
    # up
    elif dir == 6:
        ls, le = l-1, l-1
        cs, ce = c-1, c+1
    # right up
    elif dir == 7:
        ls, le = l, l+2
        cs, ce = c+2, c

    if ls in range(len(arr)) and cs in range(len(arr[0])) and le in range(len(arr)) and ce in range(len(arr[0])):
        if arr[ls][cs] == match_word[0] and arr[le][ce] == match_word[2]:
            return True

    return False


with open("./input.txt", "r") as input:
    array = []
    for line in input:
        array.append([l for l in line.strip()])

    cnt = 0
    x_cnt = 0

    for l_idx, line in enumerate(array):
        for c_idx, char in enumerate(line):
            if char == "X":
                for dir in range(8):
                    if searchWord("XMAS", array, dir, l_idx, c_idx, 1):
                        cnt += 1
            if char == "M":
                for dir in range(8):
                    if searchWord("MAS", array, dir, l_idx, c_idx, 1):
                        if searchX("MAS", array, dir, l_idx, c_idx):
                            x_cnt += 1

    print(cnt)
    print(x_cnt)
