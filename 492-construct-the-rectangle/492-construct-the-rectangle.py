class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        w = int(sqrt(area))
        size = {}
        diff = {}
        i = 0
        while w > 0:
            l = area / w
            if int(l) == l:
                size[i] = [int(l),int(w)]
                
                diff[i] = l - w
                
                i += 1
            w -= 1
        try:    
            min_ind = list(diff.values()).index(min(diff.values()))
        except:
            return [area,1]
        
        k = list(diff.keys())[min_ind]
        return size[k]
            