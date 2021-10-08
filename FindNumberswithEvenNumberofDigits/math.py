class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: int(log10(x)) % 2 == 1, nums)))
