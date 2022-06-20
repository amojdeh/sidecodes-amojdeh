class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        n = 0
        temp = x
        
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        
        else:
            while temp > 0:
                
                n = n*10 + temp % 10
                temp = temp // 10
                
        return n == x
        
        
        