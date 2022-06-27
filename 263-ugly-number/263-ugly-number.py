class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while not n%2 or not n%5 or not n%3:
            if n%2 == 0:
                n /= 2
                if n == 1:
                    return True
                else:
                    continue
            elif n%3 == 0:
                n /= 3
                if n == 1:
                    return True
                else:
                    continue
            elif n%5 == 0:
                n /= 5
                if n == 1:
                    return True
                else:
                    continue
        return False
        
            
        
            