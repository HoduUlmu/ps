import sys

read = sys.stdin.readline
n = int(read())
words = set()

for _ in range(n):
    words.add(read().strip())
words = sorted(words, key=lambda x: (len(x), x))

for word in words:
    print(word)