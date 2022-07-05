class Solution:
    def reverseWords(self, s: str) -> str:
        
        new = ''
        
        for i in s.split():
            
            new = new + i[::-1] + ' '
            
        return new[:-1]
            