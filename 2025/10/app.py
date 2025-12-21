total_presses = 0


def search(paths: list[list[list]], target: list, steps: list[list]):
    while paths:
        # Prioritize shortest path for evaluation
        paths.sort(key=lambda p: len(p))
        path = paths.pop(0)
        cur_step = path[-1]
        # Apply all button presses
        for step in steps:
            step_result = [*cur_step]
            for light in step:
                step_result[light] = not step_result[light]
            # Assess repetitions (don't add step)
            # either in the current path
            # or in any other path
            if step_result in path or any(filter(lambda p: step_result in p, paths)):
                continue
            # Assess target (return result)
            elif step_result == target:
                return path
            else:
                paths.append([*path, step_result])


with open("./input.txt", "r") as input:
    for id, line in enumerate(input):
        machine = line.rstrip().split(" ")
        target_lights = list(map(lambda l: l == "#", machine.pop(0)[1:-1]))
        start_lights = list(False for _ in range(0, len(target_lights)))
        joltage = machine.pop()[1:-1]
        buttons = list(
            map(lambda b: list(map(int, b[1:-1].split(","))), machine))

        result = search([[start_lights]], target_lights, buttons)
        total_presses += len(result)
    print("Part 1:", total_presses)
