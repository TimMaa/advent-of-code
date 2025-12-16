adjacents = [[-1, -1], [-1, 0], [-1, 1],
             [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def compute_step(grid: list):
    accessible = 0
    x_len = len(grid[0])
    y_len = len(grid)

    next_grid = [[el for el in row] for row in grid]

    for y in range(0, y_len):
        for x in range(0, x_len):
            if grid[y][x] == 1:
                cur_adj = 0
                for adj in adjacents:
                    y_check = y + adj[0]
                    x_check = x + adj[1]
                    if not (y_check < 0 or y_check > y_len - 1 or x_check < 0 or x_check > x_len - 1):
                        cur_adj += grid[y_check][x_check]
                if cur_adj < 4:
                    accessible += 1
                    next_grid[y][x] = 0

    return accessible, next_grid


with open("./input.txt", "r") as input:
    grid = [[1 if x == "@" else 0 for x in line.rstrip()] for line in input]

    removed, r_last = 0, 0
    next_grid = grid
    while True:
        r_last, next_grid = compute_step(next_grid)
        removed += r_last
        print(r_last, removed)
        if r_last == 0:
            break
