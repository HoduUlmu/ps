import collections


def solution(s):
    counter = collections.Counter(s.lower())
    return counter.get('p') == counter.get('y')


print(solution('pPooooyY'))
print(solution('ddd'))

# def numPY(s):
#     # 함수를 완성하세요
#     return s.lower().count('p') == s.lower().count('y')
