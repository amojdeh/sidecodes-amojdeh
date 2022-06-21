class Solution:
    def climbStairs(self, n: int) -> int:
        
        fib = {}
        
        fib[1] = 1
        fib[2] = 2
        
        for i in range(3,n+1):
            
            fib[i] = fib[i-1] + fib[i-2]
            
        return fib[n]