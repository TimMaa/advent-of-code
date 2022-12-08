grid = list()
visible = 0
best_score = 0

def check_dir(pos: list, height: int, vector: list):
  while True:
    pos = list(map(sum, zip(pos,vector)))
    if grid[pos[0]][pos[1]] >= height:
      return False
    if pos[0] == 0 or pos[1] == 0 or pos[0] == len(grid) - 1 or pos[1] == len(grid) - 1:
      return True

def scenic_score(pos: list, height: int, vector: list):
  score = 0
  while True:
    pos = list(map(sum, zip(pos,vector)))
    score += 1
    if grid[pos[0]][pos[1]] >= height or pos[0] == 0 or pos[1] == 0 or pos[0] == len(grid) - 1 or pos[1] == len(grid) - 1:
      return score

with open("./input.txt", "r") as input:
  for line in input:
    grid.append([int(x) for x in line.strip("\n")])

  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      # Edge Trees
      if r == 0 or c == 0 or r == len(grid) - 1 or c == len(row) - 1:
        visible += 1
        continue

      # Part 1
      if check_dir([r,c], col, [0,1]) or check_dir([r,c], col, [0,-1]) or check_dir([r,c], col, [1,0]) or check_dir([r,c], col, [-1,0]):
        visible += 1

      # Part 2
      cur_score = scenic_score([r,c], col, [0,1]) * scenic_score([r,c], col, [0,-1]) * scenic_score([r,c], col, [1,0]) * scenic_score([r,c], col, [-1,0])
      if cur_score > best_score:
        best_score = cur_score

# Part 1
print(visible)

# Part 2
print(best_score)