class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a = [ord(i) for i in set(letters)]
        a.sort()
        for i in a:
            if ord(target) < i:
                return chr(i)
        return letters[0]