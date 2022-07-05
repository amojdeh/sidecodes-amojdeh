class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if len(s) < k:
            
            return s[::-1]
        
        elif k <= len(s) <2*k:
            
            return s[0:k][::-1] + s[k:]
        
        else:
            a = list(s)
            
            for i in range(0, len(a), 2*k):
                a[i:i+k] = reversed(a[i:i+k])
                
        return "".join(a)