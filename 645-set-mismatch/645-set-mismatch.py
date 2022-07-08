class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        l = list(range(1, len(nums)+1))
        ans = []
        for i in nums:
            if i in d:
                ans.append(i)
            else:
                d[i] = 1
                
        for i in l:
            if i not in d:
                ans.append(i)
        return ans