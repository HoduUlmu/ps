import heapq


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = list(s), list(t)
        heapq.heapify(s), heapq.heapify(t)

        for _ in range(len(s)):
            if heapq.heappop(s) != heapq.heappop(t):
                return False

        return True



print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram(s = "rat", t = "car"))


