#  시간 내로 못품
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = collections.defaultdict(str)
        anagram: List = []

        for s in strs:
            sorted_s = sorted(s)
            sorted_dict[f'{sorted_s}'] += s
        print(sorted_dict)











