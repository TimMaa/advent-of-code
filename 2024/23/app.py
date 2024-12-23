sets = set()
computers = set()
comp_graph = {}

with open("./input.txt", "r") as input:
    for line in input:
        a, b = line.strip().split("-")
        sets.add((a, b))
        computers.add(a)
        computers.add(b)

for c in computers:
    comp_graph[c] = set([t for d in [con for con in sets if c in con]
                         for t in d if t != c])

for i in range(3, len(computers)):
    longest_sets = [s for s in sets if len(s) == i-1]
    if len(longest_sets) == 0:
        # Part 2
        print(",".join(sorted(max(sets, key=len))))
        break
    for elements in longest_sets:
        for cn in [c for c in computers if all(c in comp_graph[e] for e in elements)]:
            sets.add(tuple(sorted(elements + (cn,))))
    if i == 3:
        # Part 1
        print(len([s for s in sets if len(s) ==
              i and any(c[0] == "t" for c in s)]))
