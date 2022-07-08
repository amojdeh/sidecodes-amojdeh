import numpy as np
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        
        if len(nums) == 3:
            return np.prod(nums)
        
        if len(set(nums)) == 1:
            return nums[0]**3
        
        else:
            nums.sort(reverse = True)
            
            if len(nums) < 6:
                
                if all(x>0 for x in nums):
                    return nums[0]*nums[1]*nums[2]
                elif all(x<0 for x in nums):
                    return nums[0]*nums[1]*nums[2]
                else:
                    return max(nums[0]*nums[1]*nums[2],nums[0]*nums[-1]*nums[-2])
                        
                    
                    
            else:
                new = [nums[0], nums[1], nums[2], nums[-3], nums[-2], nums[-1]]
                return max(new[0]*new[1]*new[2],new[0]*new[-1]*new[-2])
                
            
                
                