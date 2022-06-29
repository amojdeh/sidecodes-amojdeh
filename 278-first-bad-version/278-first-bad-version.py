# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        down, up = 1,n
        
        while down <= up:
            
            mid = (up + down) // 2
            
            if isBadVersion(mid):
                up = mid - 1
            else: 
                down = mid + 1
            
        return down