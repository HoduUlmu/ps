import sys

read = sys.stdin.readline
test_case = int(read())

for _ in range(test_case):
    n, m = map(int, read().split())
    queue = map(int, read().split())
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))