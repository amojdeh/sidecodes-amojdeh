import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        elif len(mat) * len(mat[0]) == 1:
            return mat
        else:
            return list(np.reshape(mat, (r,c)))