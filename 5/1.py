seeds = []
maps = []

with open("input.txt") as f:
    for line in [line.rstrip() for line in f.readlines()]:
        if line.startswith("seeds:"):
            seeds = [int(x) for x in line.split(" ")[1:]]
        elif line == "":
            maps.append({})
        elif ":" in line:
            continue
        else:
            to_start, from_start, length = [int(x) for x in line.split(" ")]
            maps[-1][range(from_start, length + from_start)] = range(to_start, length + to_start)

def get_range(d, v):
    return next(iter([d[r][v - r.start] for r in d if v in r]), v)

def map_it(v):
    for map in maps:
        v = get_range(map, v)
    return v

print(min([map_it(seed) for seed in seeds]))
