lowest_point = None
ground = None

def fall_down(pos, covered):
  while pos not in covered:
    pos[1] += 1
    if pos[1] == ground:
      pos[1] -= 1
      return pos
  if [pos[0] - 1, pos[1]] not in covered:
    pos[0] -= 1
    return fall_down(pos, covered)
  if [pos[0] + 1, pos[1]] not in covered:
    pos[0] += 1
    return fall_down(pos, covered)

  pos[1] -= 1
  return pos

with open("./input.txt", "r") as input:
  covered = []
  for line in input:
    structure = []
    coords = line.strip().split("->")
    for coord in coords:
      x,y = map(int, coord.strip().split(","))
      if structure:
        last_point = structure[len(structure)-1]
        x_dis = last_point[0] - x
        y_dis = last_point[1] - y
        for i in range(abs(x_dis)-1):
          if x_dis > 0:
            structure.append([last_point[0]-i-1,y])
          if x_dis < 0:
            structure.append([last_point[0]+i+1,y])
        for i in range(abs(y_dis)-1):
          if y_dis > 0:
            structure.append([x,last_point[1]-i-1])
          if y_dis < 0:
            structure.append([x,last_point[1]+i+1])

      structure.append([x,y])
    [covered.append(el) for el in structure]

  lowest_point = max(covered, key=lambda x: x[1])[1]
  ground = max(covered, key=lambda x: x[1])[1] + 2
  sand_start = [500,0]
  rounds = 0
  on_the_ground = False

  while True:
    sand_pos = [coord for coord in sand_start]
    fall_down(sand_pos, covered)

    if not on_the_ground and sand_pos[1] > lowest_point:
      on_the_ground = True
      print(rounds)

    rounds += 1

    if sand_pos[1] == 0:
      break

    if rounds % 100 == 0:
      print(rounds)

    covered.append(sand_pos)

  print(rounds)
