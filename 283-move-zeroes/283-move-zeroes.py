class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        number = nums.count(0)
        
        for i in range(1, number+1):
            nums.remove(0)
            nums.append(0)