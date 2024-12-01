list_one = []
list_two = []
sim = 0

with open("./input.txt", "r") as input:
    for line in input:
        l1, l2 = line.split("   ")
        list_one.append(int(l1))
        list_two.append(int(l2))

    list_one.sort()
    list_two.sort()

    diff = sum(map(lambda a,b: abs(a - b), list_one, list_two))
    sim = sum(map(lambda a: list_two.count(a) * a, list_one))

    print(diff)
    print(sim)
