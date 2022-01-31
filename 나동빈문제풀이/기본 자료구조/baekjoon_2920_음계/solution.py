import sys

sound = list(map(int, sys.stdin.readline().split()))

ascending = True
descending = True


for i in range(1, 8):
    if sound[i] > sound[i - 1]:
        descending = False
    elif sound[i] < sound[i - 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
