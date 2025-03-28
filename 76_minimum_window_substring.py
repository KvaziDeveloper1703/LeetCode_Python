'''
You are given two strings s and t, of lengths m and n respectively.
Your task is to find the smallest substring of s that contains all the characters of t, including duplicates.
Return this minimum window substring. If no such substring exists, return an empty string "".

Examples:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = defaultdict(int)

        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""