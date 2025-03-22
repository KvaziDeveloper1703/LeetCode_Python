'''
You are given an array of integers citations, where citations[i] represents the number of citations a researcher received for their i‑th paper.
Return the h-index, which is defined as the maximum number h such that the researcher has at least h papers with at least h citations each.

Examples:
Input: citations = [3, 0, 6, 1, 5]
Output: 3

Input: citations = [1, 3, 1]
Output: 1
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break

        return h