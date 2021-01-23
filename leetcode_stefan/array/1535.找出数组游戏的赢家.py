import os
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        #winner_counter = {}
        #while True:
            #if arr[0] > arr[1]:
            #    arr.append(arr[1])
            #    arr.pop(1)
            #    winner= arr[0]
            #else:
            #    arr.append(arr[0])
            #    arr.pop(0)
            #    winner = arr[1]
            #if winner in winner_counter:
            #    winner_counter[winner] += 1
            #else:
            #    winner_counter[winner] = 1
            #if winner_counter[winner] >= k:
            #    return winner
        pre = arr[0]
        #cur = arr[1]
        winner_num = 0
        for i in range(1, len(arr)):
            cur = arr[i]
            if cur > pre:
                pre = cur
                winner_num = 0
            winner_num += 1
            if winner_num >= k:
                return pre
        return max(arr)


     
    

obj = Solution()
arr = [2,1,3,5,4,6,7]
#arr = [1,11,22,33,44,55,66,77,88,99]
k = 2
print(obj.getWinner(arr, k))

