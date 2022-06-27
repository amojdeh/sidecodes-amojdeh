import string as st
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(char) == t.count(char) for char in st.ascii_lowercase)
    