machines = {1: {}}
cost_a = 3
cost_b = 1


def calculate_steps(a, b, p):
    det = a[0] * b[1] - a[1] * b[0]

    if det == 0:
        return 0, 0

    det_ax = p[0] * b[1] - p[1] * b[0]
    det_ay = a[0] * p[1] - a[1] * p[0]
    x = det_ax / det
    y = det_ay / det

    return (int(x), int(y)) if x.is_integer() and y.is_integer() else (0, 0)


with open("./input.txt", "r") as input:
    cnt = 1
    for line in input:
        l = line.strip()
        if l == "":
            cnt += 1
            machines[cnt] = {}
        elif l.startswith("Button"):
            b, n, x, y = l.split(" ")
            machines[cnt][n[0]] = (int(x[2:len(x)-1]), int(y[2:]))
        else:
            p, x, y = l.split(" ")
            machines[cnt][p[0:len(p)-1]] = (int(x[2:len(x)-1]), int(y[2:]))
            offset = 10000000000000
            machines[cnt]["Prize2"] = (
                int(x[2:len(x)-1]) + offset, int(y[2:]) + offset)

total_part1 = 0
total_part2 = 0

for k, machine in machines.items():
    x, y = calculate_steps(machine["A"], machine["B"], machine["Prize"])
    total_part1 += x * cost_a + y * cost_b
    x, y = calculate_steps(machine["A"], machine["B"], machine["Prize2"])
    total_part2 += x * cost_a + y * cost_b

print(total_part1)
print(total_part2)
