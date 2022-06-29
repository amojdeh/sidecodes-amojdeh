class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        elif n == 1: return True
        
        else:
            
            while n != 1:
                n /= 4
                if n%4 and n!= 1:
                    return False
                else:
                    continue
            return n == 1