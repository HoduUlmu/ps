# 여러 최적화 시도를 해봤으나 2680ms 아래로 내려가지는 않았다
import sys


def get_max_len(tree_lst: list, need: int):
    if need == 0:
        return tree_lst[-1]

    lo = 0
    hi = 2000000000
    max_len = tree_lst[-1]

    while lo <= hi:
        mid = (lo + hi) // 2
        cut_len = get_cut_len(tree_lst, mid)

        if cut_len == need:
            return mid
        elif cut_len < need:
            hi = mid - 1
        else:
            lo = mid + 1
            max_len = mid

    return max_len


def get_cut_len(tree_lst: list, limit: int):
    return sum(x - limit for x in tree_lst if x > limit)


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    trees = list(map(int, read().split()))
    print(get_max_len(trees, M))

# import sys
#
#
# def get_max_len():
#     if m == 0:
#         return trees[-1]
#
#     lo = 0
#     hi = 2000000000
#     max_len = trees[-1]
#
#     while lo <= hi:
#         mid = (lo + hi) // 2
#
#         if get_cut_len(mid):
#             lo = mid + 1
#             max_len = mid
#         else:
#             hi = mid - 1
#
#     return max_len
#
#
# def get_cut_len(limit: int):
#     cut_len = sum(x - limit for x in trees if x > limit)
#     if cut_len == m:
#         print(limit)
#         exit()
#     return cut_len > m
#
#
# if __name__ == "__main__":
#     read = sys.stdin.readline
#     n, m = map(int, read().split())
#     trees = list(map(int, read().split()))
#     print(get_max_len())

# import sys
#
#
# def get_max_len():
#     if m == 0:
#         return trees[-1]
#
#     lo = 0
#     hi = max(trees)
#     max_len = trees[-1]
#
#     while lo <= hi:
#         mid = (lo + hi) // 2
#
#         if get_cut_len(mid):
#             lo = mid + 1
#             max_len = mid
#         else:
#             hi = mid - 1
#
#     return max_len
#
#
# def get_cut_len(limit: int):
#     cut_len = sum(x - limit for x in trees if x > limit)
#     if cut_len == m:
#         print(limit)
#         exit()
#     return cut_len > m
#
#
# if __name__ == "__main__":
#     read = sys.stdin.readline
#     n, m = map(int, read().split())
#     trees = list(map(int, read().split()))
#     print(get_max_len())


