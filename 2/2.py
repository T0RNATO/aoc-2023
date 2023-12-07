sum = 0

with open("2/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        game = line.split(": ")[1]
        highest = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for batch in game.split("; "):
            for cube in batch.split(", "):
                num, color = cube.split(" ")
                if int(num) > highest[color.rstrip()]:
                    highest[color.rstrip()] = int(num)
        power = highest["red"] * highest["green"] * highest["blue"]
        sum += power

print(sum)