def maxPower(s: str) -> int:
    cur = None
    num = 0
    maxNum = 0

    for c in s:
        if cur == None:
            maxNum = 1
            cur = c
            num = 1
        elif cur == c:
            num += 1
            if num > maxNum:
                maxNum = num
        else:
            cur = c
            num = 1

    return maxNum


s = "leetcodeeee"
print(maxPower(s))
