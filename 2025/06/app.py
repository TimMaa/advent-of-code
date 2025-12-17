from functools import reduce
import operator

lines_1 = []
lines_2 = []


def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def evaluate_problem(problem: list):
    op = problem[-1]
    if op == "+":
        return sum(map(int, problem[:-1]))
    else:
        return reduce(operator.mul, map(int, problem[:-1]), 1)

with open("./input.txt", "r") as input:
    for line in input:
        lines_1.append([v for v in line.rstrip().split(" ") if v != ""])
        lines_2.append([v for v in line if v != "\n"])
    
    problems = []
    problem = []
    for string in ["".join(n).strip() for n in trans(lines_2)]:
        if not string:
            problems.append(problem)
            problem = []
        elif string.isnumeric():
            problem.insert(0, string)
        else:
            problem.append(string[-1])
            problem.insert(0, string[:-1].strip())
    problems.append(problem)

    print("Part 1:", sum(evaluate_problem(p) for p in trans(lines_1)))
    print("Part 2:", sum(evaluate_problem(p) for p in problems))
