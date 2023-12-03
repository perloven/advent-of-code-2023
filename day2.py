import sys

lines = open('inputs/day2.in').read().split('\n')
for line in lines:
    print(line)


cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
game_sum = 0


class GameRound:
    red = 0
    green = 0
    blue = 0


def process_game_line(game_line):
    global game_sum
    game_sum += 1


def part1():
    return 1


def part2():
    return 2


ans1 = part1()
ans2 = part2()
print(f'Answer Part 1: {ans1}')
print(f'Answer Part 2: {ans2}')
