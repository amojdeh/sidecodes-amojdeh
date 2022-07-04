class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        
        
        for i in nums1:
                
            ind = nums2.index(i)
            
            if ind == len(nums2) - 1:
                ans.append(-1)
                continue

            m = max(nums2[ind:])

            if m > i:

                for j in nums2[ind:]:

                    if j > i:

                        ans.append(j)
                        break
            else:

                ans.append(-1)
        
        return ans
            
            