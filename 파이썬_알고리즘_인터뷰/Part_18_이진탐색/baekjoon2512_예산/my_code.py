import bisect
import sys


def get_max_budget(budget_request: list, country_budget: int):
    if sum(budget_request) <= country_budget:
        return budget_request[-1]

    lo = 1
    hi = budget_request[-1]
    max_budget = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        new_budget = get_new_budget(budget_request, mid)

        if new_budget == country_budget:
            return mid
        elif new_budget < country_budget:
            max_budget = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return max_budget


def get_new_budget(budget: list, limit: int):
    idx = bisect.bisect_left(budget, limit)
    return (len(budget) - idx) * limit + sum(budget[:idx])


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    input_budget_request = sorted((map(int, read().split())))
    input_country_budget = int(read())
    print(get_max_budget(input_budget_request, input_country_budget))
