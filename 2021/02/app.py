pos_1 = [0,0]
pos_2 = [0,0]
aim = 0

with open("./input.txt", "r") as input:
  for line in input:
    command = line.strip("\n")
    dir, val = command.split(" ")

    if dir == "forward":
      pos_1[0] += int(val)
      pos_2[0] += int(val)
      pos_2[1] += int(val) * aim
    elif dir == "down":
      pos_1[1] += int(val)
      aim += int(val)
    elif dir == "up":
      pos_1[1] -= int(val)
      aim -= int(val)

# Part 1
print(pos_1[0] * pos_1[1])
# Part 2
print(pos_2[0] * pos_2[1])