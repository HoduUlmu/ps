import sys


def solution(teachers, students, candidates):
    def check(obstacles: list) -> bool:
        for x, y in teachers:
            for z, q in students:
                if x == z:
                    for ox, oy in obstacles:
                        if ox == x:
                            if min(y, q) < oy < max(y, q):
                                break
                    else:
                        return False
                elif y == q:
                    for ox, oy in obstacles:
                        if oy == y:
                            if min(x, z) < ox < max(x, z):
                                break
                    else:
                        return False
        return True

    def recursive(idx: int, obstacles: list):
        if len(obstacles) == 3:
            if check(obstacles):
                print("YES")
                sys.exit()
            return

        for c in range(idx, len(candidates)):
            obstacles.append(candidates[c])
            recursive(c + 1, obstacles)
            obstacles.pop()

    if len(candidates) <= 3:
        if check(candidates):
            print("YES")
        else:
            print("NO")
        return
    else:
        recursive(0, [])
        print("NO")


if __name__ == "__main__":
    read = sys.stdin.readline

    n = int(read())
    in_students = []
    in_teachers = []

    for i in range(n):
        for j, v in enumerate(read().split()):
            if v == 'S':
                in_students.append((i, j))
            elif v == 'T':
                in_teachers.append((i, j))

    p_candidates = []
    for tx, ty in in_teachers:
        for sx, sy in in_students:
            if tx == sx:
                for i in range(min(ty, sy) + 1, max(ty, sy)):
                    if (tx, i) not in p_candidates:
                        p_candidates.append((tx, i))
            elif ty == sy:
                for i in range(min(tx, sx) + 1, max(tx, sx)):
                    if (i, ty) not in p_candidates:
                        p_candidates.append((i, ty))

    solution(in_teachers, in_students, p_candidates)
