def is_symbol(char):
    return not (char.isnumeric() or char == ".")


def check_valid_part(number, char_num):
    start_of_num = max([char_num - len(number) - 1, 0])
    return is_symbol(char) or is_symbol(line[start_of_num]) or \
         (line_num > 0 and any([is_symbol(c) for c in lines[line_num - 1][start_of_num: char_num + 1]])) or \
         (line_num < len(lines) - 1 and any([is_symbol(c) for c in lines[line_num + 1][start_of_num: char_num + 1]]))


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

    current_number = ""
    part_numbers = 0

    for line_num, line in enumerate(lines):
        for char_num, char in enumerate(line):
            if char.isnumeric():
                current_number += char
            elif current_number:
                if check_valid_part(current_number, char_num):
                    part_numbers += int(current_number)
                current_number = ""
        if current_number:
            if check_valid_part(current_number, len(line)):
                part_numbers += int(current_number)
        current_number = ""

    print(part_numbers)
