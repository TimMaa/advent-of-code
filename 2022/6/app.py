def find_marker(msg: str, length: int):
  last_chars = []
  for i, letter in enumerate(msg):
    last_chars.append(letter)
    if len(set(last_chars)) == length:
      return i+1
    if len(last_chars) > length - 1:
      last_chars.pop(0)

with open("./input.txt", "r") as input:
  msg = input.readline().strip("\n")
  # Part 1
  print(find_marker(msg, 4))
  # Part 2
  print(find_marker(msg, 14))
