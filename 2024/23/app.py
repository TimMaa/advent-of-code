sets = set()
comp_graph = {}

with open("./input.txt", "r") as input:
    for line in input:
        a, b = line.strip().split("-")
        sets.add((a, b))
        comp_graph[a] = comp_graph[a] + [b] if a in comp_graph else [b]
        comp_graph[b] = comp_graph[b] + [a] if b in comp_graph else [a]

for i in range(3, len(comp_graph)):
    longest_sets = [s for s in sets if len(s) == i-1]
    if len(longest_sets) == 0:
        # Part 2
        print(",".join(sorted(max(sets, key=len))))
        break
    for elements in longest_sets:
        for cn in [c for c in comp_graph if all(c in comp_graph[e] for e in elements)]:
            sets.add(tuple(sorted(elements + (cn,))))
    if i == 3:
        # Part 1
        print(len([s for s in sets if len(s) ==
              i and any(c[0] == "t" for c in s)]))
