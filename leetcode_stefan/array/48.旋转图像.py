#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from typing import List
import math 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        "(x, y) -> (y, n-x) # n == len(matrix)-1"
        temp = matrix[0][0]
        n = len(matrix) 
        for i in range(math.ceil(n/2)):
            for j in range(i, n-i-1):
               matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j] = matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i]
        

obj = Solution()
#matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("ori matrix:", matrix)
for line in matrix:
    print(line)
obj.rotate(matrix)
print("rotate matrix:", matrix)
for line in matrix:
    print(line)
