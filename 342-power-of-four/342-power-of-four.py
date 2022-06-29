class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        elif n == 1: return True
        
        else:
            
            while n != 1:
                if n%4:
                    return False
                else:
                    n /= 4
                    continue
            return n == 1