class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for d in nums:
            if True and d:
                c += 1
            else:
                c = 0
            m = max(m, c)

        return m
