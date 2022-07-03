class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = {}
        c = 0
        
        if 1 not in set(nums):
            return 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                if c in count:
                    count[c] += 1
                    
                else:
                    count[c] = 1
            
            elif nums[i] == 0:
                c += 1
                    
                    
        return max(list(count.values()))