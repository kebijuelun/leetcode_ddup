import os
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        squares = []
        while start <= end:
            if nums[start] * nums[end] < 0:
                if (nums[start] ** 2) > (nums[end] ** 2):
                    squares.append(nums[start] ** 2)
                    start += 1
                else:
                    squares.append(nums[end] ** 2)
                    end -= 1
            else:
                if nums[start] < 0:
                    squares.append(nums[start] ** 2)
                    start += 1
                else:
                    squares.append(nums[end] ** 2)
                    end -= 1
        return squares[::-1]

obj = Solution()
arr = [-4, -1, 0, 3, 10]
#arr = [1,11,22,33,44,55,66,77,88,99]
print(obj.sortedSquares(arr))

