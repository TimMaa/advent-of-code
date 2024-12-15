robots = []
els = []
field_x = 101
field_y = 103
time = 100

with open("./input.txt", "r") as input:
    for line in input:
        p, v = line.strip().split(" ")
        robots.append([
            tuple(map(int, p[2:].split(","))),
            tuple(map(int, v[2:].split(",")))
        ])

for rs, rv in robots:
    ex, ey = (time*rv[0] + rs[0]) % field_x, (time*rv[1] + rs[1]) % field_y
    els.append((ex, ey))


field_x -= 1
field_y -= 1

q1 = sum([1 for lx, ly in els if lx < field_x/2 and ly < field_y/2])
q2 = sum([1 for lx, ly in els if lx > field_x/2 and ly < field_y/2])
q3 = sum([1 for lx, ly in els if lx < field_x/2 and ly > field_y/2])
q4 = sum([1 for lx, ly in els if lx > field_x/2 and ly > field_y/2])


print(q1 * q2 * q3 * q4)
