class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        result = duration
        for i in range(len(timeSeries) - 1):
            result += min(timeSeries[i + 1] - timeSeries[i], duration)
        return result