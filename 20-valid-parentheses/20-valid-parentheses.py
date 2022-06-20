class Solution:
    def isValid(self, s: str) -> bool:
        
        for i in range(len(s)):
            if len(s) != 0:
                s = s.replace('()','').replace('{}','').replace('[]','')
        return len(s) == 0 