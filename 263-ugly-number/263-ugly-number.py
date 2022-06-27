class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n > 1:
    
            if n%2 == 0:
                n /= 2
                continue

            elif n%3 == 0:
                n /= 3
                continue

            elif n%5 == 0:
                n /= 5
                continue
            else:
                break

        return n == 1
        
            
        
            