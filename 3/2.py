directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 0],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

def get_number_at(x, line):
    number = ""
    start = x
    for char in line[x:]:
        if char.isnumeric():
            number += char
        else: break
    if x > 0:
        for char in line[x - 1::-1]:
            start -= 1
            if char.isnumeric():
                number = char + number
            else:
                break
    return {"num": int(number), "start": start}


def get_adjacent_numbers(x, y, lines):
    numbers = []
    for x_diff, y_diff in directions:
        new_x, new_y = (x + x_diff, y + y_diff)
        if new_x < 0 or new_x > len(lines[0]): continue
        if new_y < 0 or new_y > len(lines): continue
        char = lines[new_y][new_x]
        if char.isnumeric():
            number = get_number_at(new_x, lines[new_y])
            if number not in numbers: numbers.append(number)
    return [num["num"] for num in numbers]


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

    ratios = 0

    for line_num, line in enumerate(lines):
        for char_num, char in enumerate(line):
            if char == "*":
                numbers = get_adjacent_numbers(char_num, line_num, lines)
                if len(numbers) == 2:
                    ratios += numbers[0] * numbers[1]

    print(ratios)
