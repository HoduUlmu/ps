import sys


def keylogger(input: str):
    cursor = 0
    pw_lst = []
    for char in input:
        if char == '<' and cursor > 0:
            cursor -= 1
        elif char == '>' and cursor < len(pw_lst):
            cursor += 1
        elif char == '-':
            pw_lst.remove(pw_lst[cursor - 1])
            cursor -= 1
        elif char.isalnum():
            pw_lst.insert(cursor, char)
            cursor += 1

    print(''.join(pw_lst))


if __name__ == "__main__":
    read = sys.stdin.readline
    t = int(read())
    for _ in range(t):
        keylogger(read())
