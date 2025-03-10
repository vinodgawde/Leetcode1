class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        con = s + s
        if goal in con:
            return True
        return False