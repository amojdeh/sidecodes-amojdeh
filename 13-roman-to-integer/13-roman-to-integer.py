class Solution:
    def romanToInt(self, s: str) -> int:
        
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dig = 0
        
        for i in range(len(s)):
            
            

            if i != (len(s) -1) and ((dct[s[i+1]] / dct[s[i]]) == 5 or (dct[s[i+1]] / dct[s[i]]) == 10):
                                 
                dig -= dct[s[i]]
                
            else:
                dig += dct[s[i]]
                
                                                     
        return dig
            
            