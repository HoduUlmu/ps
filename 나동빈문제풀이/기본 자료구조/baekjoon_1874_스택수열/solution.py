# 스택에 원소를 삽입할 때는, 단순히 특정 수에 도달할 때까지 삽입하면 됩니다
# 스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인합니다.
import sys

read = sys.stdin.readline
n = int(read())

count = 1
stack = []
result = []

for i in range(1, n + 1):
    data = int(read())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))