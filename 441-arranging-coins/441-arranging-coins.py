class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        down, up = 1,n
        
        while down<=up:
            
            mid = (down+up)//2
            
            if mid*(mid+1)/2 <= n < (mid+1)*(mid+2)/2:
                return mid
            elif mid*(mid+1)/2 > n:
                up = mid - 1
            else:
                down = mid + 1
                
        
        