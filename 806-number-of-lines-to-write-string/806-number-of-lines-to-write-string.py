import string
class Solution:
    def numberOfLines(self, widths: List[int], st: str) -> List[int]:
        d = {}
        for c in st:
            if c in d:
                continue
            else:
                ind = string.ascii_lowercase.index(c)
                d[c] = widths[ind]
        s = 0
        l = 0
        for i in range(len(st)):
            s += d[st[i]]
            if s > 100:
                l += 1
                s = d[st[i]]
        if s == 0:
            return [l,100]
        else:
            return [l+1,s]