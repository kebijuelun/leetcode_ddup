import os
from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row, col = len(A), len(A[0])
        trans_A = []
        for i in range(row):
            for j in range(col):
                try:
                    trans_A[j].append(A[i][j])
                except:
                    trans_A.append([A[i][j]])
        return trans_A
solution = Solution()
#input_test = [[1,2,3],[4,5,6],[7,8,9]]
input_test = [[1,2,3],[4,5,6]]
res = solution.transpose(input_test)
print(res)


