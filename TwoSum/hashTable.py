def hashTable(nums, target):
    dict = {}
    numsTup = list(enumerate(nums))
    for idx, val in numsTup:
        diff = target - val
        print(hex(id(diff)))
        if diff in dict.keys():
            return[dict[diff], idx]
        else:
            dict[val] = idx


nums = [2, 11, 7, 15]
target = 9
print(hashTable(nums, target))
