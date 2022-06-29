class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0: return False
        elif n == 1: return True
        elif n % 3: return False
        
        else:
            while n != 1:
                n /= 3
                if n%3 and n != 1: return False
                else:
                    continue
            return n == 1