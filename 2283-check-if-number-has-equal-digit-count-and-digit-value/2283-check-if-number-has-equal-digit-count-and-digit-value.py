class Solution:
    def digitCount(self, num: str) -> bool:
        counter=Counter(num)
        for i in range(len(num)):
            if counter[f'{i}'] != int(num[i]):
                return False
        return True
        