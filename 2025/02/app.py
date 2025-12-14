import math

count_1 = 0
count_2 = 0


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


def evaluate_half(id: int):
    str_id = str(id)
    first, second = str_id[:len(str_id)//2], str_id[len(str_id)//2:]
    return id if first == second else 0


def evaluate_full(id: int):
    str_id = str(id)
    for divisor in divisorGenerator(len(str_id)):
        parts = [str_id[i:i+divisor] for i in range(0, len(str_id), divisor)]
        if len(parts) > 1 and all_equal(parts):
            return id
    return 0


with open("./input.txt", "r") as input:
    ranges = input.readline().split(",")
    for r in ranges:
        start, end = r.split("-")
        for id in range(int(start), int(end)+1):
            count_1 += evaluate_half(id)
            count_2 += evaluate_full(id)
    print(count_1)
    print(count_2)
