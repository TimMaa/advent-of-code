def calculate_next(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


total = 0
with open("./input.txt", "r") as input:
    global_seqs = {}
    for line in input:
        last_secret = int(line.strip())
        prices = [last_secret % 10]
        price_changes = [None]
        seqs = {}

        for i in range(2001):
            last_secret = calculate_next(last_secret)
            if i == 1999:
                total += last_secret
            price_changes.append(last_secret % 10 - prices[-1])
            prices.append(last_secret % 10)

        for i in range(1, len(price_changes) - 4):
            sequence = tuple(price_changes[i:i+4])
            if sequence not in seqs:
                seqs[sequence] = prices[i+3]

        for key, val in seqs.items():
            if key in global_seqs:
                global_seqs[key] = global_seqs[key] + val
            else:
                global_seqs[key] = val

print(total)
print(max(global_seqs.values()))
