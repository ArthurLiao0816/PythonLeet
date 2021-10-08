class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        copy = list(s)
        target = list(goal)
        if len(s) != len(goal):
            return False
        while True:
            if copy == target:
                return True
            else:
                tmp = copy[0]
                copy.pop(0)
                copy.append(tmp)
                if copy == list(s):
                    return False
