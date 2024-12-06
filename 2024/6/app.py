start_dir = (-1, 0)
start_loc = None
obstacles = []
rows = 0
cols = 0


def turn(obs, guard_loc, guard_dir):
    if tuple(map(sum, zip(guard_loc, guard_dir))) in obs:
        if guard_dir == (-1, 0):
            guard_dir = (0, 1)
        elif guard_dir == (0, 1):
            guard_dir = (1, 0)
        elif guard_dir == (1, 0):
            guard_dir = (0, -1)
        elif guard_dir == (0, -1):
            guard_dir = (-1, 0)
    if tuple(map(sum, zip(guard_loc, guard_dir))) in obs:
        return turn(obs, guard_loc, guard_dir)
    return guard_dir


def calculate_path(obs, g_loc, g_dir):
    visited_locations = []
    loop_recorder = []

    while True:
        if g_loc not in visited_locations:
            visited_locations.append(g_loc)

        if g_loc + g_dir in loop_recorder:
            return -1

        loop_recorder.append(g_loc + g_dir)

        g_dir = turn(obs, g_loc, g_dir)
        g_loc = tuple(
            map(sum, zip(g_loc, g_dir)))

        if g_loc[0] not in range(0, rows) or g_loc[1] not in range(0, cols):
            break

    return visited_locations


with open("./input.txt", "r") as input:
    for li, line in enumerate(input):
        rows += 1
        cols = len(line)
        for ci, c in enumerate(line.strip()):
            if c == "#":
                obstacles.append((li, ci))
            if c == "^":
                start_loc = (li, ci)

normal_path = calculate_path(obstacles, start_loc, start_dir)
print(len(normal_path))

loop_spots = 0
normal_path.remove(start_loc)

for loc in normal_path:
    temp_obs = [o for o in obstacles]
    temp_obs.append(loc)
    if calculate_path(temp_obs, start_loc, start_dir) == -1:
        loop_spots += 1

print(loop_spots)
