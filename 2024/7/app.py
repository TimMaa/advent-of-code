import operator
import itertools


def run_permutations(operators, result, base, operands):
    permutations = list(itertools.product(
        operators, repeat=len(operands)))

    for p in permutations:
        p_result = base
        for i, o in enumerate(p):
            if o == operator.concat:
                p_result = int(o(str(p_result), str(operands[i])))
            else:
                p_result = o(p_result, operands[i])
        if p_result == result:
            return result

    return 0


with open("./input.txt", "r") as input:
    part1_total = 0
    part2_total = 0

    for line in input:
        result, base, *operands = map(
            int, line.strip().replace(":", "").split(" "))

        part1_total += run_permutations([operator.add,
                                        operator.mul], result, base, operands)

        part2_total += run_permutations([operator.add, operator.mul,
                                        operator.concat], result, base, operands)

    print(part1_total)
    print(part2_total)
