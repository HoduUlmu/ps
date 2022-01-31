# n제곱은 25억이 나오므로 시간 초과일듯
# 68ms, 14.5MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = {}
        p1 = 0
        p2 = 0
        max_len = 0
        sub_len = 0
        while p1 < len(s) and p2 < len(s):
            if alpha.get(s[p2]) is None:
                alpha[s[p2]] = True
                sub_len += 1
                p2 += 1
            else:
                max_len = max(max_len, sub_len)
                if s[p1] == s[p2]:
                    p2 += 1
                    p1 += 1
                else:
                    while s[p1] != s[p2]:
                        alpha[s[p1]] = None
                        sub_len -= 1
                        p1 += 1
                    p1 += 1
                    p2 += 1
        max_len = max(max_len, sub_len)

        return max_len


Solution().lengthOfLongestSubstring('abcabcbb')
Solution().lengthOfLongestSubstring('bbbbb')
Solution().lengthOfLongestSubstring('pwwkew')
Solution().lengthOfLongestSubstring('p')
Solution().lengthOfLongestSubstring('')
Solution().lengthOfLongestSubstring('au')
Solution().lengthOfLongestSubstring('dvdf')
