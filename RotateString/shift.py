class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        elif len(s) != len(goal):
            return False
        else:
            for _ in range(len(s)):
                s = s[1:]+s[0]
                if s == goal:
                    return True
        return False
