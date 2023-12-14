nodes = {}

with open('input.txt') as f:
    data = f.read().splitlines()
    directions = data[0]

    for line in data[2:]:
        name, paths = line.split(" = ")
        nodes[name] = paths[1:-1].split(", ")

node = "AAA"
steps = 0

while True:
    if node == "ZZZ": break
    node = nodes[node][directions[steps % len(directions)] == "R"]
    steps += 1

print(steps)
