import re

stacks_1, stacks_2 = dict(), dict()
stacks_parsed = False

with open("./input.txt", "r") as input:
  for line in input:
    row = line.strip("\n")
    if not stacks_parsed:
      if row[:1] == " ":
        stacks_2 = {key: value[:] for key, value in stacks_1.items()}
        stacks_parsed = True
      else:
        for i, position in enumerate(range(1, len(row), 4)):
          try:
            if row[position] != " ":
              stacks_1[i+1].insert(0, row[position])
          except KeyError:
            stacks_1[i+1] = []
            stacks_1[i+1].append(row[position])
      continue

    if row != "":
      amount, source, target = map(int, re.findall(r'\d+', row))
      for _ in range(int(amount)):
        stacks_1[target].append(stacks_1[source].pop())
      stacks_2[target] = stacks_2[target] + [stacks_2[source].pop() for _ in range(int(amount))][::-1]

print("".join([stacks_1[stack].pop() for stack in range(1,len(stacks_1)+1)]))
print("".join([stacks_2[stack].pop() for stack in range(1,len(stacks_2)+1)]))