class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        if not len(score):
            return score
        sorted_score = []
        sorted_score[:] = score
        sorted_score.sort()
        
        
        
        for i in sorted_score:
        
            ind = score.index(i)
            if i == sorted_score[-1]:
                score[ind] = 'Gold Medal'
            elif i == sorted_score[-2]:
                score[ind] = 'Silver Medal'
            elif i == sorted_score[-3]:
                score[ind] = 'Bronze Medal'
            else:
                score[ind] = str(len(score) - sorted_score.index(i) )
        return score