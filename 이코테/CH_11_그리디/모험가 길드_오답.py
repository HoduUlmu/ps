# 문제 이해를 잘못함 틀림

import sys

read = sys.stdin.readline

N = int(read())
fear_list = sorted(list(map(int, read().split())))

group_num = 0

while fear_list and fear_list[-1] <= len(fear_list):
    for _ in range(fear_list[-1]):
        fear_list.pop()
    group_num += 1

print(group_num)
