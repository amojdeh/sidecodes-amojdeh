class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
    ############ s.strip() can be used to remove spaces in the beginning and end of the string: s.strip().split()[-1]############