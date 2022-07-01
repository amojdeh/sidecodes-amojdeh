class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums)) < 3:
            return max(nums)
        
        else:
            n = 1
            while(n < 3):
                m = max(nums)
                nums.remove(m)
                if not len(nums):
                    break
                while max(nums) == m:
                    nums.remove(m)
                    continue
                else:
                    m = max(nums)
                    n += 1
                    continue
                    
        return m
                
            
                
                
                

            