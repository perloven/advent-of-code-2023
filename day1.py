import sys

lines = open('inputs/day1.in').read().split('\n')


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


spelled_digits = {
    '0': 0,
    'zero': 0,
    '1': 1,
    'one': 1,
    '2': 2,
    'two': 2,
    '3': 3,
    'three': 3,
    '4': 4,
    'four': 4,
    '5': 5,
    'five': 5,
    '6': 6,
    'six': 6,
    '7': 7,
    'seven': 7,
    '8': 8,
    'eight': 8,
    '9': 9,
    'nine': 9
}


def find_first_spelled_digit(line):
    key_name = ''
    first_index = sys.maxsize
    for key, value in spelled_digits.items():
        found_index = line.find(key)
        if found_index != -1 and found_index < first_index:
            key_name = key
            first_index = found_index
    return spelled_digits.get(key_name)


def find_last_spelled_digit(line):
    key_name = ''
    first_index = sys.maxsize
    for key, value in spelled_digits.items():
        found_index = line[::-1].find(key[::-1])
        if found_index != -1 and found_index < first_index:
            key_name = key
            first_index = found_index
    return spelled_digits.get(key_name)


def part2():
    calibration_values = []
    for line in lines:
        first = find_first_spelled_digit(line)
        last = find_last_spelled_digit(line)
        calibration_values.append(str(first) + str(last))

    ans2 = 0
    for calVal in calibration_values:
        ans2 += int(calVal)
    return ans2

ans1 = part1()
ans2 = part2()
print(f'Answer Part 1: {ans1}')
print(f'Answer Part 2: {ans2}')
