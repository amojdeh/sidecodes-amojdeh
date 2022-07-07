class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        if max(nums) == min(nums):
            return 0
        
        elif max(nums) - min(nums) == 1:
            return len(nums)
        
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        
        ans = []
        
        for i in d:
            if i + 1 in d:
                ans.append(d[i] + d[i+1])
            continue
        try:
            return max(ans)
        except:
            return 0