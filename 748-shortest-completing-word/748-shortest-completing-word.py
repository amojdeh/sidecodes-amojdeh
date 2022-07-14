from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = []
        for i in licensePlate:
            if i.lower().isalpha():
                lp.append(i.lower())
        d = dict(Counter(lp))
        ans = []
        for word in words:
            if len(words) < len(lp):
                continue
            else:
                n = Counter(word)
                k = 0
            
                for i in d:
                    if i not in n:
                        break
                    else:
                        if n[i] < d[i]:
                            break
                        else:
                            k += 1
                            if k == len(d):
                                ans.append(word)
                            else:
                                continue
            out = 'sssssssssssssssss'
            for word in ans:
                if len(word) < len(out):
                    out = word
        return out