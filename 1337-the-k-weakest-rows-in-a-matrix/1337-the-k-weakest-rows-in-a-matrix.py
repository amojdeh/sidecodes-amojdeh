import numpy as np
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        weakest = []
        l = np.shape(mat)[1]
        dic = {}
        
        for i in range(len(mat)):
            
            dic[i] = sum(mat[i])
            
        sort_dic = sorted(dic.items(), key=lambda x: x[1])
        
        weakest = [i[0] for i in sort_dic]
        return weakest[:k]