import re

sensors = []
beacons = []

def calc_dis(x_1, y_1, x_2, y_2):
  return abs(x_1 - x_2) + abs(y_1 - y_2)

def h_diff(sensor, row):
  return (sensor[2] - (abs(sensor[1] - row)))

def solve_row(y, bounds=[]):
  if not bounds:
    # Calculate lower and upper bounds
    bounds.append(min(map(lambda s: s[0] - h_diff(s, y), sensors)))
    bounds.append(max(map(lambda s: s[0] + h_diff(s, y), sensors)))
  return jump_solve(y, [bounds[0], bounds[1]]) - len(list(filter(lambda b: b[1] == y, beacons)))

def jump_solve(y, bounds) -> int:
  next_blocked = 0
  closest_sensors = list(filter(lambda s: calc_dis(s[0], s[1], bounds[0], y) <= s[2], sensors))

  if len(closest_sensors):
    cs = closest_sensors[0]
    next_blocked = h_diff(cs, y) + cs[0] - bounds[0] + 1
  else:
    if bounds[0] > bounds[1]:
      return 0
    else:
      print("OPEN SPOT")
      print([bounds[0], y])
      print(bounds[0] * 4000000 + y)
      return 0 + jump_solve(y, [bounds[0] + 1, bounds[1]])

  return next_blocked if bounds[0] == bounds[1] else next_blocked + jump_solve(y, [bounds[0] + next_blocked, bounds[1]])

with open("./input.txt", "r") as input:
  for line in input:
    sx, sy, bx, by = map(int, re.findall("-*\d+", line))
    dis = calc_dis(sx, sy, bx, by)
    sensors.append([sx, sy, dis])
    beacons.append((bx, by))

  beacons = set(beacons)

print(solve_row(2000000))
for y in range(0,4000001):
  res = solve_row(y, [0, 4000000])