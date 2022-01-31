import sys

sound = list(map(int, sys.stdin.readline().split()))
if sorted(sound) == sound:
    print("ascending")
elif sorted(sound, reverse=True) == sound:
    print("descending")
else:
    print("mixed")


