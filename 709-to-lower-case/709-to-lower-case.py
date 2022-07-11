class Solution:
    def toLowerCase(self, s: str) -> str:
        new = ''
        for i in s:
            if 65 <= ord(i) <= 90:
                new += chr(ord(i)+32)
            else:
                new += i
        return new