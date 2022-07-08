class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        
        else:
            
            m = s = sum(nums[:k])
            
            for i in range(k, len(nums)):
                s += (nums[i] - nums[i-k])
                
                if s > m: 
                    m = s
                    
            return m / k