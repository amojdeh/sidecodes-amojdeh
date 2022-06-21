class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] < 9:
        #     d = digits[-1]
        #     digits.pop()
        #     digits.append(d + 1)
        #     return digits
        
        s = ""
        for item in digits:
            s += str(item)
            
        new = int(s) + 1
        
        return list(str(new))