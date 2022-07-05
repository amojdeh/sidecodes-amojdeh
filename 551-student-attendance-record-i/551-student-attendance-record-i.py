class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if len(s) <=2:
            if s != 'AA':
                return True
            
        if s.count('A') < 2:
            if 'LLL' not in s:
                return True
        return False
                        
                        