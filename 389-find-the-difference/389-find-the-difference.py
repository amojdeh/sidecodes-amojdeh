class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        t_list = list(t)
        for i in list(s):
            t_list.remove(i)
            
        return ''.join(t_list)
        
            