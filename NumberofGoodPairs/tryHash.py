class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = {}
        counter = 0
        for num in nums:
            if num not in table:
                table[num] = 0
            else:
                table[num] += 1
                counter += table[num]
        return counter


# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         table = {}
#         counter = 0
#         for num in nums:
#             counter += table.setdefault(num, 0)
#             table[num] += 1
#         return counter
