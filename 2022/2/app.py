elves = list()

points_1: dict = {
  "X": 1,
  "Y": 2,
  "Z": 3,
  "A X": 3,
  "A Y": 6,
  "A Z": 0,
  "B X": 0,
  "B Y": 3,
  "B Z": 6,
  "C X": 6,
  "C Y": 0,
  "C Z": 3,
}
points_2: dict = {
  "A X": 3,
  "A Y": 4,
  "A Z": 8,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 2,
  "C Y": 6,
  "C Z": 7,
}

score_1 = 0
score_2 = 0

with open("./input.txt", "r") as input:
  for line in input:
    round = line.strip("\n")
    score_1 += points_1[round[2:]]
    score_1 += points_1[round]

    score_2 += points_2[round]


# Part 1
print(score_1)
# Part 2
print(score_2)