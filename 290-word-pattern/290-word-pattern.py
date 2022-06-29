class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    
        
        if len(set(list(pattern))) != len(set(s.split())): return False
        
        if len(pattern) != len(s.split()): return False
        
        if len(set(zip(pattern,s.split()))) == len(set(list(pattern))): return True
        return False