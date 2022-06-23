import string as st
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            char = (columnNumber) % 26
            res += st.ascii_uppercase[char - 1]
            print(res)
            columnNumber = (columnNumber-1)//26
            
        return res[::-1]