class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        def xor_list(x):
            return [i^1 for i in x]
        def rev(x):
            x.reverse()
            return x
        ans = [rev(x) for x in image]
        ans = [xor_list(x) for x in ans]
        
        return ans