# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        down, up = 1, n
        
        while down <= up:
            
            mid = (down + up) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                down = mid + 1
            elif guess(mid) == -1:
                up = mid
        return down
            
                