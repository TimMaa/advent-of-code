machines = {1: {}}
cost_a = 3
cost_b = 1

def dfs(machine, current_vertex, visited, cost):
    # Overshot
    if current_vertex[0] > machine["Prize"][0] or current_vertex[1] > machine["Prize"][1] or cost > 400:
        return None

    if current_vertex == machine["Prize"]:
        return visited, cost

    visited.append(current_vertex)
    a = tuple(map(sum, zip(current_vertex, machine["A"])))
    b = tuple(map(sum, zip(current_vertex, machine["B"])))

    # Check for paths through b first, as it would generally be cheaper
    if b not in visited:
        path = dfs(machine, b, visited, cost + cost_b)
        if path:
            return path
    if a not in visited:
        path = dfs(machine, a, visited, cost + cost_a)
        if path:
            return path


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

# Part 1
total = 0
for k, machine in machines.items():
    if (machine["A"][0] + machine["B"][0]) * 100 > machine["Prize"][0] and (machine["A"][1] + machine["B"][1]) * 100 > machine["Prize"][1]:
      path = dfs(machine, (0,0), [], 0)
      if path:
          total += path[1]
print(total)
