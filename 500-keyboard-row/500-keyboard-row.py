
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first = list("qwertyuiop")
        second = list("asdfghjkl")
        third = list("zxcvbnm")
        
        ans = []
        
        for word in words:
            
            if all(char in first for char in list(word.lower())):
                ans.append(word)
                continue
            if all(char in second for char in list(word.lower())):
                ans.append(word)
                continue
            if all(char in third for char in list(word.lower())):
                ans.append(word)
                continue
        return ans