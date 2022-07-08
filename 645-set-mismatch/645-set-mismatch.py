class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        l = list(range(1, len(nums)+1))
        print(l)
        ans = []
        for i in l:
            if i not in nums:
                ans.append(i)
        for i in nums:
            if i in d:
                return [i, ans[0]]
            else:
                d[i] = 1