import sys


def solution(key, lock):
    holes = [(i, j) for i, row in enumerate(lock) for j, x in enumerate(row) if x == 0]

    for _ in range(4):
        key = [[*k[::-1]] for k in zip(*key)]
        pops = [(i + 1 - len(key), j) for i, row in enumerate(key) for j, x in enumerate(row) if x == 1]

        for j in range(1 - len(key), len(lock)):
            for i in range(1 - len(key), len(lock)):
                check = 0
                for pop in pops:
                    if (pop[0], pop[1] + i) in holes:
                        check += 1
                    elif -1 < pop[1] + i < len(lock) and -1 < pop[0] < len(lock):
                        check = 0
                        break
                if check == len(holes):
                    return True
            pops = [(a + 1, b) for a, b in pops]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

