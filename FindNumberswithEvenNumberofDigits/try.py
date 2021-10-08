from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            dig = 0
            while num:
                num //= 10
                dig += 1
            if dig % 2 == 0:
                counter += 1
        return counter
