class Solution:
    def findComplement(self, num: int) -> int:
        new = ''
        for i in bin(num)[2:]:
            
            if i == '1':
                new += '0'
            elif i == '0':
                new += '1'
    
        return int(new, 2)