import bisect
import sys


def get_max_len(tree_lst: list, need: int):
    if need == 0:
        return tree_lst[-1]

    lo = 0
    hi = tree_lst[-1]
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
    idx = bisect.bisect_left(tree_lst, limit)
    return sum(tree_lst[x] - limit for x in range(idx, len(tree_lst)))


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    trees = sorted(map(int, read().split()))
    print(get_max_len(trees, M))
