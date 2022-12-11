strength_sum = 0
draw_cache = []
offset = 1

def eval_signal(cycle: int, x: int):
  return cycle * x if cycle % 40 == 20 else 0

# Part 2
def draw(draw_cache: list, cycle: int, x: int):
  global offset
  draw_cache.append("#" if cycle-offset in range(x-1, x+2) else ".")
  if cycle % 40 == 0 and cycle != 0:
    print("".join(draw_cache))
    offset += 40
    draw_cache.clear()

with open("./input.txt", "r") as input:
  cycle = 0
  x = 1

  for line in input:
    command = line.strip("\n").split()
    cycle += 1
    draw(draw_cache, cycle, x)
    strength_sum += eval_signal(cycle, x)

    if command[0] == "noop":
      continue

    cycle += 1
    draw(draw_cache, cycle, x)
    strength_sum += eval_signal(cycle, x)
    x += int(command[1])

# Part 1
print(strength_sum)