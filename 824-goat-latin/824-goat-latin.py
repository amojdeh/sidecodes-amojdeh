class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        s = sentence.split()
        for i in range(len(s)):
            if s[i][0].lower() in ['a','e','i','u','o']:
                ans.append(s[i] + 'ma' + 'a'*(i+1))
            else:
                ans.append(s[i][1:] + s[i][0] + 'ma' + 'a'*(i+1))
        return ' '.join(ans)
                