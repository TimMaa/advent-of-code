cur_dir: list[str] = []
directory_sizes: dict = dict()
max_space = 70000000
req_space = 30000000

def add_to_dir_size(path: list[str], size: int):
  directory_sizes["/".join(path)] += size
  path.pop()
  if len(path) != 0:
    add_to_dir_size(path, size)

with open("./input.txt", "r") as input:
  for line in input:
    terminal = line.strip("\n").split(" ")
    if terminal[1] == "cd":
      if terminal[2] == "..":
        cur_dir.pop()
      elif terminal[2] == "/":
        cur_dir.append("root")
        directory_sizes["root"] = 0
      else:
        cur_dir.append(terminal[2])
    elif terminal[0] == "dir":
      directory_sizes["/".join(cur_dir) + "/" + terminal[1]] = 0
    elif terminal[0].isnumeric():
      add_to_dir_size(cur_dir.copy(), int(terminal[0]))

  sum = 0
  size_to_delete = directory_sizes["root"] - (max_space - req_space)
  smallest_dir = max_space

  for dir in directory_sizes.values():
    if dir < 100000:
      sum += dir
    if dir > size_to_delete and dir < smallest_dir:
      smallest_dir = dir

# Part 1
print(sum)
# # Part 2
print(smallest_dir)