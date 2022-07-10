class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        
        for i in ops:
            
            try:
                score.append(int(i))
            except:
                if i == 'C':
                    score.pop()
                elif i == 'D':
                    score.append(score[-1]*2)
                elif i == '+':
                    score.append(score[-1]+ score[-2])
        return sum(score)