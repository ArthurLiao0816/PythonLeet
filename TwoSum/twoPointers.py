def twoSum(nums, target):
    start = 0
    end = len(nums)-1

    newList = list(zip(nums, range(len(nums))))
    newList.sort()

    for i in range(len(nums)):
        sumTmp = newList[start][0]+newList[end][0]
        if sumTmp > target:
            end += -1
        elif sumTmp < target:
            start += 1
        else:
            return [newList[start][1], newList[end][1]]


nums = [2, 11, 7, 15]
target = 9
print(twoSum(nums, target))
