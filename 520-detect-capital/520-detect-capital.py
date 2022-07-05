class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1:
            return True
        
        if word.isupper():
            return True
        
        elif word[1:].islower():
            return True
        else:
            return False
            