'''
You are given a string s and an array of strings words. All the words are of the same length.
A concatenated substring is a substring of s that consists of all the words in words concatenated together in any order, without any extra characters. Each word must appear exactly once.
Return a list of starting indices in s where such concatenated substrings begin. The order of the output does not matter.

Examples:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
'''

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(word_count):
                word_start = i + j * word_len
                word = s[word_start : word_start + word_len]
                if word not in word_map:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_map[word]:
                    break
            else:
                result.append(i)

        return result