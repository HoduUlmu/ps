import re


class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]