from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict(Counter(stones))
        jewel = 0
        for stone in d:
            if stone in jewels:
                jewel += d[stone]
        return jewel