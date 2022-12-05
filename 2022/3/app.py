sum = 0
group = []
badge_sum = 0

def val(item: str):
  return ord(item) - 96 if ord(item) > 96 else ord(item) - 38

with open("./input.txt", "r") as input:
  for i, line in enumerate(input):
    rucksack = line.strip("\n")
    sum += val((set(rucksack[:int(len(rucksack)/2)]) & set(rucksack[int(len(rucksack)/2):])).pop())

    group.append(rucksack)
    if (i+1)%3 == 0:
      badge_sum += val((set(group[0]) & set(group[1]) & set(group[2])).pop())
      group.clear()

# Part 1
print(sum)
#Part 2
print(badge_sum)