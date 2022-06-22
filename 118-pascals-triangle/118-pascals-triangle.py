class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = {}
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        pascal[1] = [1]
        pascal[2] = [1,1]
        
        for i in range(3,numRows+1):
            pascal[i] = []
            for j in range(i):
                if j == 0:
                    pascal[i].append(1)
                elif j == i - 1:
                    pascal[i].append(1)
                else:
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        return list(pascal.values())
            
            