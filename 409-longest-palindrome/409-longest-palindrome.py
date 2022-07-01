class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        elif len(set(list(s))) == 1:
            return len(s)
        
        l = {}
        z = -1
        for i in s:
            
            if i in l:
                continue
            else:
                l[i] = s.count(i)
                if s.count(i) % 2 == 1:
                    z += 1
        if z != -1:
            
            return sum(list(l.values())) - z
        else: 
            return sum(list(l.values()))