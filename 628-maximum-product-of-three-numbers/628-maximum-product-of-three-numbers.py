import numpy as np
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        
        if len(nums) == 3:
            return np.prod(nums)
        
        if len(set(nums)) == 1:
            return nums[0]**3
        
        else:
            nums.sort(reverse = True)
            return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])
                
                