class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(set(s)) == len(s):
            return False
        elif len(set(s)) == 1:

            return True
        else:
            
            sub = ''
            
            for i in s:
                sub += i
                if len(sub) == len(s):
                    return False
                if sub * (len(s)//len(sub)) == s:
                    return True
                
                else:
                    continue
        return False