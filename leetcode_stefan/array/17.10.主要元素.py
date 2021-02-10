import os
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        elif len(nums) == 1:
            return nums[0]
        else:
            sort_nums = sorted(nums)
            length = len(nums)
            for start in range(0, len(nums)//2+1): 
                end = start + length // 2
                if sort_nums[start] == sort_nums[end]:
                    return sort_nums[start]
                else:
                    continue
            return -1
    def majorityElement_v2(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        elif len(nums) == 1:
            return nums[0]
        else:
            num_set = {}
            for num in nums:
                try:
                    num_set[num] += 1
                except:
                    num_set[num] = 1
            for k, v in num_set.items():
                if v > len(nums)//2:
                    return k
            return -1
    def majorityElement_v3(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        elif len(nums) == 1:
            return nums[0]
        else:
            count = 0
            for num in nums:
                if count <= 0:

                    
            

obj = Solution()
# in_test = [1,2,5,9,5,9,5,5,5]
in_test = [2,2,1,1,1,2,2]
print(obj.majorityElement_v2(in_test))
