order = []
updates = []
ok = 0
not_ok = 0


def order_page(order: list, update: list):
    new_update = []
    for p in update:
        target_index = -1
        relevant_orders = list(filter(lambda o: o[0] == p, order))
        for ro in relevant_orders:
            if ro[1] in new_update:
                cond_idx = new_update.index(ro[1])
                if cond_idx < target_index or target_index == -1:
                    target_index = cond_idx
        if target_index == -1:
            new_update.append(p)
        else:
            new_update.insert(target_index, p)

    return new_update[round((len(update)-1)/2)]


with open("./input.txt", "r") as input:
    for line in input:
        instruction = line.strip().split("|")
        if len(instruction) == 2:
            order.append([int(instruction[0]), int(instruction[1])])
        elif len(instruction[0]) > 2:
            updates.append(list(map(int, instruction[0].split(","))))

for update in updates:
    is_good = True
    already_printed = []
    for page in update:
        for o in order:
            if page == o[0] and o[1] in already_printed:
                is_good = False
                not_ok += order_page(order, update)
                break
        if not is_good:
            break
        already_printed.append(page)
    if is_good:
        ok += update[round((len(update)-1)/2)]

print(ok)
print(not_ok)
