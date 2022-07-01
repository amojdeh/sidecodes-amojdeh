class Solution:
    def countSegments(self, s: str) -> int:
        # return len(s.split())
        
        count, last = 0, ' '
        
        for i in s:
            
            if i != ' ' and last == ' ':
                count += 1
            last = i
    
        return count