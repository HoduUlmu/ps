# 52MS 14.4MB
import collections
import re
from typing import List


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)

        # most_common은 왜 1부터?
        return counts.most_common(1)[0][0]


