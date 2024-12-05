order = []
updates = []
ok = 0
not_ok = 0


def order_page(order: list, update: list):
    relevant_orders = list(
        filter(lambda o: o[0] in update and o[1] in update, order))
    new_order = []
    for ro in relevant_orders:
        # if ro[0] not in new_order:
        #   new_order.append(ro[0])
        # if ro[1] in new_order:
        #   new_order.remove(ro[1])
        #   new_order.append(ro[1])
        if ro[1] in new_order:
            if ro[0] in new_order:
                if new_order.index(ro[0]) > new_order.index(ro[1]):
                    new_order.remove(ro[0])
                    new_order.insert(new_order.index(ro[1]), ro[0])
            else:
                new_order.insert(new_order.index(ro[1]), ro[0])

        else:
            if ro[0] not in new_order:
                new_order.append(ro[0])
            new_order.append(ro[1])
    print(new_order[round((len(update)-1)/2)])
    return new_order[round((len(update)-1)/2)]


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
