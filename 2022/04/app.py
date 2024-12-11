contained = 0
overlaps = 0

with open("./input.txt", "r") as input:
  for line in input:
    assignment = line.strip("\n")
    elf_1, elf_2 = [list(map(int, elf.split("-"))) for elf in assignment.split(",")]
    if (elf_1[1] >= elf_2[0] and elf_1[0] <= elf_2[1]) or (elf_2[1] >= elf_1[0] and elf_2[0] <= elf_1[1]):
      overlaps += 1
      if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or (elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]):
        contained += 1

# Part 1
print(contained)
#Part 2
print(overlaps)