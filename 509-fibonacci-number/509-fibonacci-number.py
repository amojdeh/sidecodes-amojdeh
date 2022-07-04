class Solution:
    def fib(self, n: int) -> int:
        
        F = {0: 0, 1: 1}
        
        if n in [0,1]:
            return F[n]
            
        for i in range(2,n+1):
            F[i] = F[i-1] + F[i-2]
                
        return F[n]