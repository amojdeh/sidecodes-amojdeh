class Solution:
    def mySqrt(self, x: int) -> int:
        
        ######## my code ##########
#         i = 0
        
#         while True:
            
#             if i*i == x:
#                 return i
#             elif i*i < x < (i+1)*(i+1):
#                 return i
            
#             i += 1

######### optimal solution #########

        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                if mid == left:
                    return mid
                left = mid
            else:
                return mid
        return None