class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        ind = nums.index(m)
        nums.remove(m)
        if max(nums) == 0:
            return ind
        else:
            if m / max(nums) >= 2:
                return ind
            else:
                return -1