prev = 9999999
higher_1 = 0
higher_2 = 0
prev_win = []
curr_win = []

with open("./input.txt", "r") as input:
  for line in input:
    val = int(line.strip("\n"))
    if val > prev:
      higher_1 += 1
    prev = val

    if len(prev_win) != 0:
      curr_win.append(val)
    if len(prev_win) < 3:
      prev_win.append(val)


    if len(curr_win) == 3:
      if sum(prev_win) < sum(curr_win):
        higher_2 += 1
      prev_win.pop(0)
      curr_win.pop(0)
      prev_win.append(curr_win[1])



# Part 1
print(higher_1)
# Part 2
print(higher_2)