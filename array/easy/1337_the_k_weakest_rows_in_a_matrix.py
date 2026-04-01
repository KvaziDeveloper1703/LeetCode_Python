'''
You are given an m x n binary matrix mat consisting of:
    - 1 — representing soldiers;
    - 0 — representing civilians.
In each row, all the soldiers appear to the left of the civilians.

A row i is considered weaker than a row j if:
    - The number of soldiers in row i is less than in row j, or
    - Both rows have the same number of soldiers, but i < j.

Return the indices of the k weakest rows in the matrix, ordered from weakest to strongest.

Examples:
Input: mat = [  [1,1,0,0,0],
                [1,1,1,1,0],
                [1,0,0,0,0],
                [1,1,0,0,0],
                [1,1,1,1,1]
        ]
k = 3
Output: [2,0,3]

Input: mat = [  [1,0,0,0],
                [1,1,1,1],
                [1,0,0,0],
                [1,0,0,0]
        ]
k = 2
Output: [0,2]
'''

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        
        for index in range(len(mat)):
            soldiers = sum(mat[index])
            rows.append((soldiers, index))
        
        rows.sort()
        
        result = []
        for i in range(k):
            result.append(rows[i][1])
        
        return result

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k = 3

solution = Solution()
print(solution.kWeakestRows(mat, k))