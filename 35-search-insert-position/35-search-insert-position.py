class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i = 1
            ind = None
            while ind == None:
                if target - i in nums:
                    ind = nums.index(target-i)
                    return ind + 1
                elif target + i in nums:
                    ind = nums.index(target + i)
                    return ind
                i += 1
                    
    ############ simple solution
    
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         nums.append(target)
    #         nums.sort()
    #         return nums.index(target)