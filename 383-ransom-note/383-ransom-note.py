class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        
        if len(magazine) < len(ransomNote):
            return False
        
        else:
            for i in ransomNote:
                if ransomNote.count(i) > magazine.count(i):
                    return False
        return True
                    
############### python counter is good for these cases #############