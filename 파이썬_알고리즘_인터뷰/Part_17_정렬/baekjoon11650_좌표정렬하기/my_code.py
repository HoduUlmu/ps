import sys


def quicksort(start, end):
    def partition(ps, pe):
        pivot = pe
        i = ps - 1

        for j in range(ps, pe):
            if (coordinate[j][0] < coordinate[pivot][0]) or \
                    (coordinate[j][0] == coordinate[pivot][0] and coordinate[j][1] < coordinate[pivot][1]):
                i += 1
                coordinate[j], coordinate[i] = coordinate[i], coordinate[j]

        coordinate[i + 1], coordinate[pivot] = coordinate[pivot], coordinate[i + 1]
        return i + 1

    if start >= end:
        return None

    p = partition(start, end)
    quicksort(start, p -1)
    quicksort(p + 1, end)


read = sys.stdin.readline
n = int(read())
# 좌표를 tuple 형태로 묶음
coordinate = [tuple(map(int, read().split())) for _ in range(n)]
quicksort(0, len(coordinate) - 1)

for i in coordinate:
    print(i[0], i[1])