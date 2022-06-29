class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        if num == 1:
            return True
        
        else:
            down, up = 1, num // 2
            
            while down <= up:
                
                mid = (down + up) // 2
                if mid*mid == num:
                    return True
                elif mid*mid < num:
                    down = mid + 1
                else:
                    up = mid - 1
            return False