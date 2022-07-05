class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if len(s) <=2:
            if s != 'AA':
                return True
            
            
        
        if s.count('A') < 2:
            
            for i in range(len(s)):
                
                if s[i] == 'L':
                    if i != 0 and i != len(s) - 1:
                        if s[i-1] == 'L' and s[i+1] == 'L':
                            return False
                    elif i == 0:
                        if s[2] == 'L' and s[1] == 'L':
                            return False
                    elif i == len(s) - 1:
                        if s[-2] == 'L' and s[-3] == 'L':
                            return False
            return True
        return False
                        
                        