class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        result = []
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums2:
            if i in d and d[i]>0:
                result.append(i)
                d[i]-=1
        return result