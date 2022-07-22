class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        answer = []
        for i in range(len(s)):
            if s[i] == c:
                l.append(i)
                
        for i in range(len(s)):
            if s[i] == c:
                answer.append(0)
            else:
                answer.append(min([abs(i - x) for x in l]))
        return answer
                
            
            