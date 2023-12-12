total = 0
number_strings = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("input.txt") as input_data:
    for line in [line.rstrip() for line in input_data.readlines()]:
        nums = []
        for i, search_pass in enumerate([line, line[::-1]]):
            partial_num = ""
            for char in search_pass:
                if char.isnumeric():
                    nums.append(char)
                    break
                for possibility in [[partial_num + char, partial_num[-1] + char if partial_num else "&", char], [char + partial_num, char + partial_num[0] if partial_num else "&", char]][i]:
                    if any((word.endswith(possibility) if i else word.startswith(possibility)) for word in number_strings.keys()):
                        partial_num = possibility
                        if partial_num in number_strings:
                            nums.append(number_strings[partial_num])
                        break
                else:
                    partial_num = ""
                if len(nums) > i: break
        total += int("".join(nums))
print(total)
