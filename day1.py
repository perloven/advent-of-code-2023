import sys

lines = open(sys.argv[1]).read().split('\n')


def part1():
    calibration_values = []
    for line in lines:
        first = find_first_digit(line)
        last = find_last_digit(line)
        calibration_values.append(str(first) + str(last))

    ans1 = 0
    for calVal in calibration_values:
        ans1 += int(calVal)
    return ans1


def find_first_digit(line):
    for char in line:
        if char.isnumeric():
            return int(char)


def find_last_digit(line):
    for char in reversed(line):
        if char.isnumeric():
            return int(char)


ans1 = part1()
ans2 = 0
print(f'Answer Part 1: {ans1}')
print(f'Answer Part 2: {ans2}')