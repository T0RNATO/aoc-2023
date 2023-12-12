total = 0
with open("input.txt") as f:
    for line in [line.rstrip() for line in f.readlines()]:
        sections = line.split(":")[1].split("|")
        intersection = len(set([int(number.strip()) for number in sections[0].split(" ") if number.strip().isnumeric()]).intersection([int(number.strip()) for number in sections[1].split(" ") if number.strip().isnumeric()]))
        if intersection > 0: total += 2 ** (intersection - 1)
print(total)
