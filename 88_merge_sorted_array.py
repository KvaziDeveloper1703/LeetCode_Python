'''
You are given two integer arrays, nums1 and nums2, both sorted in non-decreasing order, and two integers, m and n, representing the number of valid elements in nums1 and nums2, respectively.
Your task is to merge nums2 into nums1 as one sorted array in-place.
+ nums1 has a length of m + n, where:
    + The first m elements contain the elements to be merged.
    + The last n elements are set to 0 and should be ignored.
+ nums2 has exactly n elements.

Requirements:
+ Merge nums2 into nums1, so that nums1 becomes a sorted array of size m + n.
+ Do not return the merged array — modify nums1 in-place.

Examples:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Output:
nums1 = [1,2,2,3,5,6]

Input:
nums1 = [1], m = 1
nums2 = [], n = 0
Output:
nums1 = [1]

Example 3
Input:
nums1 = [0], m = 0
nums2 = [1], n = 1
Output:
nums1 = [1]
'''