class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif len(s) == 0:
            return False
        else:
            return goal in s+s