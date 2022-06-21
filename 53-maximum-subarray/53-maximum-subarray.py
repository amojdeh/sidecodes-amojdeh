class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subsum = 0
        tempsum = 0
        sumlist = []
        
        if all(i < 0 for i in nums):
            return max(nums)
        
        if len(nums) == 1:
            return nums[0]
        if not len(nums):
            return 0
        
        
        else:
            for i in range(len(nums)):
                tempsum += nums[i]
                if tempsum >= subsum or tempsum > 0:
                    subsum = tempsum
                    sumlist.append(subsum)
                else:
                    subsum = 0
                    tempsum = 0
                    continue
        return max(sumlist)