# 66ms, 14.5MB
# 나는 중복 문자가 발생 했을 시 해당 위치까지 일일이 비교하며 이동했는데 이걸 딕셔너리에 index 값을 넣어서 한번에 처리하다니...
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        print(max_length)
        return max_length


Solution().lengthOfLongestSubstring('dvdfd')