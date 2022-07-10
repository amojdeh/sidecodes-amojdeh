class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if len(set(nums)) == 1:
            return 1
        
        else:
            count = 1
            l = []
            for i in range(len(nums)):
                if i != len(nums) - 1:
                    if nums[i+1] > nums[i]:
                        count += 1
                    else:
                        l.append(count)
                        count = 1
                else:
                    if nums[-1] > nums[-2]:
                        l.append(count)
                    else:
                        l.append(1)
            return max(l)