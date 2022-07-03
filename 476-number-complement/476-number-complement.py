class Solution:
    def findComplement(self, num: int) -> int:
#         new = ''
#         for i in bin(num)[2:]:
            
#             if i == '1':
#                 new += '0'
#             elif i == '0':
#                 new += '1'
    
#         return int(new, 2)
    
    
        new = ''.join('1' if x == '0' else '0' for x in bin(num)[2:])
        return int(new,2)