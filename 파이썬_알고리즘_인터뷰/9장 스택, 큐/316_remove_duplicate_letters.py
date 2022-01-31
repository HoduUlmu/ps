import collections
from typing import Deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # 각 문자 갯수를 측정하는 카운터
        # 각 문자의 종복읋 확인하는 set
        # 새 문자열 받을 stack
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1

            # 중복 문자 확인
            if char in seen:
                continue

            # 스택에 값이 있고
            # 스택 제일 위의 값이 현 for문 문자보다 사전순으로 뒤에 있고
            # counter에 문자가 하나 이상 있는 문자인 경우
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)


Solution().removeDuplicateLetters('bcabc')
