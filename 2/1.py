max = {"red": 12,"green": 13,"blue": 14}
valid_count = 0
with open("2/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        game = line.split(": ")[1]
        valid = True
        for batch in game.split("; "):
            for cube in batch.split(", "):
                num, color = cube.split(" ")
                if int(num) > max[color.rstrip()]:
                    valid = False
                    break
        if valid:
            valid_count += i + 1
print(valid_count)