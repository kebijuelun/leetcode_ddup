import os
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i+1):
                sub_arr = arr[j: j+i]
                res += sum(sub_arr)
        return res
                        

obj = Solution()
arr = [1,4,2,5,3]
#arr = [1,11,22,33,44,55,66,77,88,99]
print(obj.sumOddLengthSubarrays(arr))

