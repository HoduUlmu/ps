# 57ms , 14.6 MB
class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        left_p = 0
        right_p = len(s) - 1

        while left_p < right_p:
            if not s[left_p].isalnum():
                left_p += 1
                continue
            elif not s[right_p].isalnum():
                right_p -= 1
                continue

            if s[left_p] != s[right_p]:
                return False

            left_p += 1
            right_p -= 1
        return True

