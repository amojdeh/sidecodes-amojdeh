import string as st
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            print(col_num)
            col_num = col_num*26 + st.ascii_uppercase.index(char) + 1
        return col_num