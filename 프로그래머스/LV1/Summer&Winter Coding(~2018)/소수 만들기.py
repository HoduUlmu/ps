def solution(nums):
    cand_set = []

    def recursive(cand, flag):
        if len(cand) == 3:
            cand_set.append(sum(cand))
            return

        for i in range(flag, len(nums)):
            cand.append(nums[i])
            recursive(cand, i + 1)
            cand.pop()

    def is_prime(n):
        for i in range(2, int(n ** 0.5 + 1)):
            if not n % i:
                return False
        return True

    recursive([], 0)
    ans = 0
    for num in cand_set:
        if is_prime(num):
            ans += 1
    return ans


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))

# from itertools import combinations
# def prime_number(x):
#     answer = 0
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             answer+=1
#     return 1 if answer==1 else 0
#
# def solution(nums):
#     return sum([prime_number(sum(c)) for c in combinations(nums,3)])
