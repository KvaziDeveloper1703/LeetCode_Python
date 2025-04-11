'''
You are given a 0-indexed array of integers numbers of length n. You start at the first element numbers[0].
Each element numbers[i] represents the maximum number of steps you can jump forward from index i. In other words, from index i, you can jump to any index in the range [i + 1, i + numbers[i]], as long as it is within bounds (i + j < n).
Your task is to return the minimum number of jumps required to reach the last index (numbers[n - 1]).
You can assume that it is always possible to reach the last index.

Examples:
Input: numbers = [2, 3, 1, 1, 4]
Output: 2

Input: numbers = [2, 3, 0, 1, 4]
Output: 2
'''

from typing import List

def jump(numbers: List[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(numbers) - 1):
        farthest = max(farthest, i + numbers[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps