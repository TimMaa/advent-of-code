elves = list()

with open("./day_1_input.txt", "r") as input:
  cur_elf_cal = 0
  for line in input:
    try:
      cur_elf_cal += int(line)
    except ValueError:
      elves.append(cur_elf_cal)
      cur_elf_cal = 0

elves.sort(reverse=True)
# Full list for verification
print(elves)
# Part 1
print(elves[0])
#Part 2
print(sum(elves[:3]))