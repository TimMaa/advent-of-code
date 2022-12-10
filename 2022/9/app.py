def simulate(length: int):
  rope = []
  positions = set()

  for _ in range(length):
    rope.append([0,0])

  with open("./input.txt", "r") as input:
    for line in input:
      dir, count = line.strip("\n").split(" ")
      for _ in range(int(count)):
        # Move Head
        if dir == "L":
          rope[0][0] -= 1
        elif dir == "R":
          rope[0][0] += 1
        elif dir == "U":
          rope[0][1] -= 1
        elif dir == "D":
          rope[0][1] += 1
        # Move Knots
        for k in range(len(rope)-1):
          distance = [x-y for x,y in zip(rope[k], rope[k+1])]
          norm_distance = list(map(lambda x: int(x/abs(x)) if x!= 0 else 0, distance))
          if abs(distance[0]) > 1 or abs(distance[1]) > 1:
            rope[k+1] = list(map(sum, zip(rope[k+1], norm_distance)))

        positions.add(",".join(map(str, rope[-1:][0])))

  return positions

# Draw the pattern
def draw(positions: list):
  max = [0,0]
  min = [0,0]

  for pos_str in positions:
    pos = pos_str.split(",")
    if int(pos[0]) > max[0]:
      max[0] = int(pos[0])
    elif int(pos[0]) < min[0]:
      min[0] = int(pos[0])
    if int(pos[1]) > max[1]:
      max[1] = int(pos[1])
    elif int(pos[1]) < min[1]:
      min[1] = int(pos[1])

  for k in range(min[1],max[1]+1):
    output = ""
    for i in range(min[0],max[0]+1):
      if i == 0 and k == 0:
        output += "s"
      elif ",".join(map(str, [i,k])) in positions:
        output += "#"
      else:
        output += "."
    print(output)

# Part 1
run_2 = simulate(2)
draw(run_2)
print(len(run_2))

# Part 2
run_10 = simulate(10)
draw(run_10)
print(len(run_10))