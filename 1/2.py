total = 0
number_strings = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("input.txt") as input_data:
    for line in [line.rstrip() for line in input_data.readlines()]:
        num1 = num2 = ""
        partial_num = ""
        for char in line:
            if char.isnumeric():
                num1 = char
                break

            for possibility in [partial_num + char, partial_num[-1] + char if partial_num else "&", char]:
                if any(word.startswith(possibility) for word in number_strings.keys()):
                    partial_num = possibility
                    if partial_num in number_strings:
                        num1 = number_strings[partial_num]
                    break
            else:
                partial_num = ""
            if num1: break
        partial_num = ""
        for char in line[::-1]:
            if char.isnumeric():
                num2 += char
                break

            for possibility in [char + partial_num, char + partial_num[0] if partial_num else "&", char]:
                if any(word.endswith(possibility) for word in number_strings.keys()):
                    partial_num = possibility
                    if partial_num in number_strings:
                        num2 += number_strings[partial_num]
                    break
            else:
                partial_num = ""
            if num2: break
        total += int(num1 + num2)
        print(int(num1 + num2))
print(total)
