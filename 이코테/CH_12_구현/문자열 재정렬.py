import functools
import sys


def compare(s1: str, s2: str):
    if s1.isalpha() and s2.isnumeric():
        return -1
    elif s1.isnumeric() and s2.isalpha():
        return 1
    elif s1 > s2:
        return 1
    else:
        return -1


s = sorted(list(sys.stdin.readline().strip()), key=functools.cmp_to_key(compare))
print(s)
