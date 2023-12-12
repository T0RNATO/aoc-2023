copies = {}

def inc(i):
    if i in copies: copies[i] += 1
    else: copies[i] = 1

with open("input.txt") as f:
    for i, line in enumerate([line.rstrip() for line in f.readlines()]):
        inc(i)
        sections = line.split(":")[1].split("|")
        intersection = len(set([int(number.strip()) for number in sections[0].split(" ") if number.strip().isnumeric()]).intersection([int(number.strip()) for number in sections[1].split(" ") if number.strip().isnumeric()]))
        for _ in range(copies[i]):
            for j in range(1, intersection + 1):
                inc(i + j)

print(sum(copies.values()))
