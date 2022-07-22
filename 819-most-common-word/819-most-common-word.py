import operator
from collections import Counter
class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        
        s = s.replace("!", ' ').replace("?", ' ').replace("'", ' ').replace(",", ' ').replace(";", ' ').replace(".", ' ').lower()
        
        d = dict(Counter(s.split()))
        banned = set(banned)
        k = max(d.items(), key=operator.itemgetter(1))[0]
        while k in banned:
            d.pop(k)
            k = max(d.items(), key=operator.itemgetter(1))[0]
        return k
            