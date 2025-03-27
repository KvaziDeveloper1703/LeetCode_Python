'''
There are n children standing in a line, and each child has a rating represented by the integer array ratings.
You need to distribute candies to these children based on the following rules:
+ Every child must receive at least one candy.
+ A child with a higher rating than an immediate neighbor must receive more candies than that neighbor.

Your task is to determine the minimum number of candies needed to distribute to all the children while satisfying these rules.

Examples:
Input: ratings = [1, 0, 2]
Output: 5

Input: ratings = [1, 2, 2]
Output: 4
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)