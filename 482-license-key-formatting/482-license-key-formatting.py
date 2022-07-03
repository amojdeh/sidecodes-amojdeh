class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        new_s = ''.join(s.split('-')).upper()
        
        if len(new_s) == 1:
            return new_s
        
        if k >= len(new_s):
            return new_s
        
        first = len(new_s) % k 
        
        length = len(new_s) // k
        
        new = new_s[:first]
        if len(new):
            new += '-'
            
        for i in range(length):
            for j in range(k):
                new += new_s[first + i*k + j]

                if j == k - 1:
                    new+='-'
        return new[:-1]
            
            
        
        