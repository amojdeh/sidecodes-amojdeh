import string as st
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        new_s = ''
        for i in s:
            new_s += str(st.ascii_lowercase.index(i) + 1)
        print(new_s)
        
        while k > 0:
            
            count = sum(int(i) for i in new_s)    
            k -= 1
            new_s = str(count)
        return count