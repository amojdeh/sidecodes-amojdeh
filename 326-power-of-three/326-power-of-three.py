class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0: return False
        if n == 1: return True
        if n % 3: return False
        
        while n != 1:
            n /= 3
            if n%3 and n != 1: return False
            else:
                continue
        return n == 1