import math
from typing import List


# 에라토스테네스의 체
def solution(n):
    is_prime = [1] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if is_prime[i]:
            is_prime[i + i::i] = [0] * ((n - i) // i)
    return len([x for x in range(2, len(is_prime)) if is_prime[x]])


print(solution(10))
print(solution(5))

# #
# def primes_up_to_good(n: int) -> List[int]:
#     seive = [0] * 2 + [1] * (n - 1)
#     # print(sys.getsizeof(seive))
#     for k in range(2, int(n ** 0.5 + 1.5)):
#         if seive[k]:
#             seive[k * 2::k] = [0] * ((n - k) // k)
#     return [x for x in range(n + 1) if seive[x]]

# def solution(n):
#     num=set(range(2,n+1))
#
#     for i in range(2, int(n ** 0.5 + 1):
#         if i in num:
#             num-=set(range(i*i,n+1,i))
#     return len(num)