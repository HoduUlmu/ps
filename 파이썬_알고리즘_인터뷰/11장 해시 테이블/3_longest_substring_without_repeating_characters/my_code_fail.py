# 실패 dvdf 같은 경우를 고려하지 못했다
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        alpha = {}
        max_len = 0
        sub_len = 0

        for idx, char in enumerate(s):
            if alpha.get(char) is None:
                alpha[char] = True
                sub_len += 1
            else:
                alpha = {}
                max_len = max(max_len, sub_len)
                alpha[char] = True
                sub_len = 1

        max_len = max(max_len, sub_len)
        return max_len


Solution().lengthOfLongestSubstring('abcabcbb')
Solution().lengthOfLongestSubstring('bbbbb')
Solution().lengthOfLongestSubstring('pwwkew')
Solution().lengthOfLongestSubstring('p')
Solution().lengthOfLongestSubstring('')
Solution().lengthOfLongestSubstring('au')
Solution().lengthOfLongestSubstring('dvdf')
