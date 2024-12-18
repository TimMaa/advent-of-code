robots = []
field_x = 101
field_y = 103

with open("./input.txt", "r") as input:
    for line in input:
        p, v = line.strip().split(" ")
        robots.append([
            tuple(map(int, p[2:].split(","))),
            tuple(map(int, v[2:].split(",")))
        ])

els = [((100*rv[0] + rs[0]) % field_x, (100*rv[1] + rs[1]) % field_y)
       for rs, rv in robots]
q1 = sum([1 for lx, ly in els if lx < field_x//2 and ly < field_y//2])
q2 = sum([1 for lx, ly in els if lx > field_x//2 and ly < field_y//2])
q3 = sum([1 for lx, ly in els if lx < field_x//2 and ly > field_y//2])
q4 = sum([1 for lx, ly in els if lx > field_x//2 and ly > field_y//2])
print(q1 * q2 * q3 * q4)

for t in range(0, field_x*field_y):
    layout = set([((t*rv[0] + rs[0]) % field_x, (t*rv[1] + rs[1]) % field_y)
                  for rs, rv in robots])
    neighbors = 0
    for robot in layout:
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          if tuple(map(sum, zip(robot, d))) in layout:
              neighbors += 1

    if neighbors > 1000:
      for x in range(field_x):
          for y in range(field_y):
              print("*", end="") if (x, y) in layout else print(".", end="")
          print("")
      print("t:", t)
      break
