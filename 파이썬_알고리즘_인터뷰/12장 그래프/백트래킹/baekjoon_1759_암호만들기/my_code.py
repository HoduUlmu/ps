import sys

input = sys.stdin.readline
l, c = map(int, input().split())
alpha_list = sorted(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']


def is_vowel(s: str) -> bool:
    cnt = 0
    for v in vowel:
        if v in s:
            cnt += 1

    if 0 < cnt < len(s) - 1:
        return True

    return False


def recursive(n: int, possible_pw: str) -> None:
    if len(possible_pw) >= l:
        if is_vowel(possible_pw):
            print(possible_pw)
        return

    for index in range(n, c):
        possible_pw += alpha_list[index]
        recursive(index + 1, possible_pw)
        possible_pw = possible_pw[:-1]


recursive(0, '')
