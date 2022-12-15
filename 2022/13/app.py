import itertools
import functools

all_packets = [[[2]], [[6]]]

def compare_pair(left: list, right: list):
  for l, r in itertools.zip_longest(left, right):
    if l is None:
      return -1
    if r is None:
      return 1
    if type(l) is int and type(r) is int:
      if r < l:
        return 1
      elif l < r:
        return -1
      else:
        continue
    if type(l) is int and type(r) is list:
      result = compare_pair([l], r)
    if type(l) is list:
      result = compare_pair(l,r) if type(r) is list else compare_pair(l, [r])
    if result == 0:
      continue
    else:
      return result

  return 0

with open("./input.txt", "r") as input:
  left = None
  right = None
  pair_index = 0
  sum = 0

  for line in input:
    packet = line.strip()
    if not packet:
      continue
    elif left == None:
      left = eval(packet)
    else:
      right = eval(packet)
      pair_index += 1
      if compare_pair(left, right) == -1:
        sum += pair_index
      all_packets.append(left)
      all_packets.append(right)
      left = None
      right = None

all_packets.sort(key=functools.cmp_to_key(compare_pair))

# Part 1
print(sum)

# Part 2
print((all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1))