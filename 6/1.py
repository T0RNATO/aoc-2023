import math

# I can't be bothered doing parsing, so I'll just hardcode the input
races = [
    {"time": 45, "record": 305},
    {"time": 97, "record": 1062},
    {"time": 72, "record": 1110},
    {"time": 95, "record": 1695}
]

winning_options = []

for race in races:
    winning_options.append(0)
    for i in range(race["time"]):
        distance = i * (race["time"] - i)
        if distance > race["record"]:
            winning_options[-1] += 1

print(math.prod(winning_options))
