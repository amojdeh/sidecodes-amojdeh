class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num < 0:
            
            s = '-'
            
        elif 0 <= num < 7:
            return str(num)
        
        else:
            s = ''
            
        num = abs(num)
        st = ''
        
        while num >= 7:
            
            st += str(num%7)
            
            num //= 7
        
        st += str(num)
        
        return s + st[::-1]