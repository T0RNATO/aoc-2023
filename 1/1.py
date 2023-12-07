total = 0
with open("input.txt") as input:
    for line in input.readlines():
        nums = []
        for char in line[:-1]:
            if char.isnumeric():
                nums.append(char)
        total += int(nums[0] + nums[-1])
print(total)