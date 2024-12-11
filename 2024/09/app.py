sequence = []
sorted_sequence = []
file_list = []
sorted_index = []


with open("./input.txt", "r") as input:
    for line in input:
        for i, c in enumerate(line):
            if i % 2 == 0:
                for x in range(0, int(c)):
                    sequence.append(int(i/2))
                file_list.append((int(c), int(i/2)))
            else:
                for x in range(0, int(c)):
                    sequence.append(-1)
                file_list.append((int(c), -1))

for i in sequence:
    if i == -1:
        last_el = -1
        while last_el == -1:
            last_el = sequence.pop()
        sorted_sequence.append(last_el)
    else:
        sorted_sequence.append(i)

checksum_part_1 = sum([i * b for i, b in enumerate(sorted_sequence)])
print(checksum_part_1)

for file in reversed([x for x in file_list if x[1] != -1]):
    original_spot = file_list.index(file)
    gap = next((y for y in file_list if y[1] == -1 and y[0] >= file[0]), None)
    if gap:
        free_spot = file_list.index(gap)
        if free_spot < original_spot:
            file_list.remove(gap)
            file_list.remove(file)
            file_list.insert(free_spot, file)
            file_list.insert(original_spot, (file[0], -1))
            if gap[0] - file[0] > 0:
                file_list.insert(free_spot + 1, (gap[0] - file[0], -1))

checksum_part_2 = 0
blocks = []

print("CHECK")

for f in file_list:
    for c in range(0, f[0]):
        blocks.append(f[1])
for idx, b in enumerate(blocks):
    if b != -1:
        checksum_part_2 += idx * b

print(checksum_part_2)
