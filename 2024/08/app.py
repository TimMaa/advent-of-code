import itertools

rows = 0
cols = 0
anomalies = set()
harmonies = set()


def get_anomalies(start, diff, harmonic=False):
    anomaly = tuple(map(sum, zip(diff, start)))
    if anomaly[0] in range(0, rows) and anomaly[1] in range(0, cols):
        if harmonic:
            return [anomaly] + get_anomalies(anomaly, diff, True)
        else:
            return [anomaly]
    return []


with open("./input.txt", "r") as input:
    antennas = {}
    for li, line in enumerate(input):
        rows += 1
        cols = len(line)

        for ci, c in enumerate(line.strip()):
            if c != ".":
                a_pos = (li, ci)
                if c in antennas.keys():
                    antennas[c].append(a_pos)
                else:
                    antennas[c] = [a_pos]
                harmonies.add(a_pos)

    for set in antennas.values():
        for perm in itertools.permutations(set, r=2):
            diff_vector = (perm[0][0] - perm[1][0], perm[0][1] - perm[1][1])
            for a in get_anomalies(perm[0], diff_vector):
                anomalies.add(a)
            for a in get_anomalies(perm[0], diff_vector, True):
                harmonies.add(a)

    print(len(anomalies))
    print(len(harmonies))
