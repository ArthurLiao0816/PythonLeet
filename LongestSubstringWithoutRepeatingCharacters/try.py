s = "pwwkew"


def lengthOfLongestSubstring(s: str) -> int:
    if not len(s):
        return 0

    maxLen = len(set(s))
    sLen = len(s)

    for tLen in reversed(range(1, maxLen+1)):
        steps = sLen-tLen+1
        isAns = False
        for step in range(steps):
            car = s[step:step+tLen]
            print(car)
            if len(set(car)) == tLen:
                isAns = True
        if isAns:
            return tLen
    return 1


print(lengthOfLongestSubstring(s))
