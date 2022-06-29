class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = []
        
        for i in nums1:
            if i in nums2:
                if i in d:
                    continue
                else:
                    d.append(i)
                    
        return d