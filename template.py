import sys

lines = open(sys.argv[1]).read().split('\n')
for line in lines:
    print(line)

ans1 = 0
ans2 = 0
print(f'Answer Part 1: {ans1}')
print(f'Answer Part 2: {ans2}')
