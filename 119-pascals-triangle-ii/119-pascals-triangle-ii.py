class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascal = {}
        pascal[1] = [1]
        pascal[2] = [1,1]
        
        for i in range(3,rowIndex + 2):
            pascal[i] = []
            for j in range(i):
                if j == 0:
                    pascal[i].append(1)
                elif j == i - 1:
                    pascal[i].append(1)
                else:
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
                    
        return pascal[rowIndex + 1]
            