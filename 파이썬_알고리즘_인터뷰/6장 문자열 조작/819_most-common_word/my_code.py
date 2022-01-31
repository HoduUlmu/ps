# 53ms , 14.4MB
import collections
import re
from typing import List


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower().split()

        words = collections.defaultdict(int)

        for word in paragraph:
            if word in banned:
                continue
            words[word] += 1

        return max(words, key=words.get)
