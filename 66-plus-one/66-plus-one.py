class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        s = ""
        for item in digits:
            s += str(item)
            
        new = int(s) + 1
        
        return list(str(new))