from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if len(ans) == 0:
                ans.append(num)
            else:
                ans.append(ans[-1]+num)
        return ans


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ans = []
#         tmp = 0
#         for num in nums:
#             tmp += num
#             ans.append(tmp)
#         return ans


solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))
