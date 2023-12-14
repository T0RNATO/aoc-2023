import math

nodes = {}

with open('input.txt') as f:
    data = f.read().splitlines()
    directions = data[0]

    for line in data[2:]:
        name, paths = line.split(" = ")
        nodes[name] = paths[1:-1].split(", ")

current_nodes = [node for node in nodes if node[2] == "A"]
steps = 0

loops = [0, 0, 0, 0, 0, 0]

while True:
    direction = directions[steps % len(directions)] == "R"
    for i, node in enumerate(current_nodes):
        current_nodes[i] = nodes[node][direction]
        if current_nodes[i][2] == "Z":  # Find the step count at which each of the start points reaches its end
            loops[i] = steps + 1  # Add one just for fun, not sure why it's needed
            if all(loops):  # Once all the end points are found, calculate the LCM to find where they intersect
                print(math.lcm(*loops))
                exit()
    steps += 1
