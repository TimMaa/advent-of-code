class Monkey:
  def __init__(self):
    self.items = []
    self.inspections = 0

  def check_items(self, monkeys: dict, divisor: int, modulo: int):
    for item in self.items:
      worry = eval(self.operation, {"old": item}) % modulo
      worry = worry // divisor
      monkeys[self.target_true if worry % self.test == 0 else self.target_false].items.append(worry)
      self.inspections += 1
    self.items.clear()

def simulate(divisor: int, rounds: int, do_modulo: bool):
  monkeys = dict()

  with open("./input.txt", "r") as input:
    current_monkey: Monkey = None
    for line in input:
      note = line.strip()
      if not note:
        continue
      elif note.startswith("Monkey"):
        monkeys[note[-2]] = Monkey()
        current_monkey = monkeys[note[-2]]
      elif note.startswith("Starting"):
        for item in note.split(" "):
          try:
            current_monkey.items.append(int(item.strip(",")))
          except:
            continue
      elif note.startswith("Operation"):
        current_monkey.operation = note.split(":")[1].split("=")[1]
      elif note.startswith("Test"):
        current_monkey.test = int(note.split(" ")[-1])
      elif note.startswith("If true"):
        current_monkey.target_true = note.split(" ")[-1]
      elif note.startswith("If false"):
        current_monkey.target_false = note.split(" ")[-1]

  modulo = 1
  for monkey in monkeys.values():
    modulo *= monkey.test

  for _ in range(rounds):
      [monkey.check_items(monkeys, divisor, modulo) for monkey in monkeys.values()]

  inspections = sorted([monkey.inspections for monkey in monkeys.values()], reverse=True)
  print(inspections[0] * inspections[1])

simulate(3, 20, False)
simulate(1, 10000, True)