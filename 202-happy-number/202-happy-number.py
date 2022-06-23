class Solution:
    def isHappy(self, n: int) -> bool:
        sum_square = 0
        seen = []
        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            else: 
                seen.append(n)
                n = sum(int(i)**2 for i in str(n))