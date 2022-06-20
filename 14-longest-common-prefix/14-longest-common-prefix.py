class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""  
        # print(tuple(zip(*strs))
        for w in zip(*strs):
            
            if len(set(w)) == 1:
                result += w[0]
            else:
                return result
        return result
                