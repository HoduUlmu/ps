# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# input : 4
# output : 1+1+1+1, 1+1+2, 1+2+1,
#          2+1+1, 2+2, 1+3, 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.


# make(4) = make(3) + make(2) + make(1)
import sys


def make(n):
    if n == 1:
        return 1  # 1을 만드는 경우의 수 1가지 [1]
    if n == 2:
        return 2  # 2을 만드는 경우의 수 2가지 [1, 1], [2]
    if n == 3:
        return 4  # 3을 만드는 경우의 수 4가지 [1, 1, 1] [2, 2] [1, 3] [3, 1]
    return make(n - 1) + make(n - 2) + make(n - 3)


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    case = int(input())
    print(make(case))
