zeros = []
ones = []
gamma = ""
epsilon = ""
o2_gen = ""
co2_scrub = ""

with open("./input.txt", "r") as input:
  for line in input:
    bin = line.strip("\n")
    if len(zeros) == 0:
      for _ in bin:
        zeros.append(0)
        ones.append(0)
    for i, char in enumerate(bin):
      if char == "0":
        zeros[i] += 1
      else:
        ones[i] += 1

  for i, count in enumerate(zeros):
    if count > ones[i]:
      gamma += "0"
      epsilon += "1"
    else:
      gamma += "1"
      epsilon += "0"

# Part 1
print(int(gamma, 2) * int(epsilon, 2))
# Part 1
print(epsilon)