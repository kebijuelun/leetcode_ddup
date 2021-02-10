import os
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        else:
            s = sorted(nums)
            return max(s[0] * s[1] * s[-1], s[-1] * s[-2] * s[-3])
                        


solution = Solution()
input_test = [1,2,3,4]
# input_test = [-1, -2, -3, -4]
res = solution.maximumProduct(input_test)
print(res)
