class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        else:
            
            F = {0: 0, 1: 1}
            
            for i in range(2,n+1):
                F[i] = F[i-1] + F[i-2]
                
        return F[n]