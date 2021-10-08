def maxPower(s: str) -> int:
    pointer = None
    num = 0
    maxNum = 0

    for c in s:
        if pointer == c:
            num += 1
        else:
            pointer = c
            num = 1
        maxNum = max(maxNum, num)

    return maxNum


s = "leetcodeeee"
print(maxPower(s))
